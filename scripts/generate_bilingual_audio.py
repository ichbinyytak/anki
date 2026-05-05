#!/usr/bin/env python3
import argparse
import asyncio
import hashlib
import json
import random
import time
from pathlib import Path

import edge_tts
import lameenc
from mutagen.mp3 import MP3


def load_entries(input_path):
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    if isinstance(payload, list):
        words = payload
    elif isinstance(payload, dict) and isinstance(payload.get("words"), list):
        words = payload["words"]
    else:
        raise ValueError("Input must be a JSON array or an object with a words array.")

    required = ["word", "wordTranslation", "example", "translation"]
    entries = []
    for index, item in enumerate(words, start=1):
        missing = [field for field in required if not str(item.get(field, "")).strip()]
        if missing:
            raise ValueError(f"Item #{index} missing fields: {', '.join(missing)}")
        entries.append([
            str(item["word"]).strip(),
            str(item["wordTranslation"]).strip(),
            str(item["example"]).strip(),
            str(item["translation"]).strip(),
        ])
    return entries


def silence_mp3(seconds, sample_rate=24000, channels=1, bit_rate=48):
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(bit_rate)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)

    sample_count = int(sample_rate * seconds)
    pcm = b"\x00\x00" * sample_count * channels
    return encoder.encode(pcm) + encoder.flush()


def cache_name(index, part_index, text, voice, rate):
    digest = hashlib.sha256(f"{voice}\0{rate}\0{text}".encode("utf-8")).hexdigest()[:16]
    return f"{index:04d}_{part_index}_{digest}.mp3"


async def save_tts(text, output, voice, rate):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(str(output))


async def save_tts_with_retry(text, output, voice, rate, retries, retry_delay):
    if output.exists() and output.stat().st_size > 0:
        return

    last_error = None
    for attempt in range(1, retries + 1):
        try:
            await save_tts(text, output, voice, rate)
            if output.stat().st_size == 0:
                raise RuntimeError(f"{output} is empty")
            return
        except Exception as error:
            last_error = error
            output.unlink(missing_ok=True)
            if attempt == retries:
                break
            sleep_for = retry_delay * attempt + random.uniform(0, 1.5)
            print(f"retry {attempt}/{retries} after TTS error: {error}", flush=True)
            await asyncio.sleep(sleep_for)

    raise RuntimeError(f"failed to generate {output}: {last_error}")


async def generate_segments(entries, voice, rate, cache_dir, retries, retry_delay):
    segments = []
    for index, parts in enumerate(entries, start=1):
        paths = []
        for part_index, text in enumerate(parts, start=1):
            path = cache_dir / cache_name(index, part_index, text, voice, rate)
            await save_tts_with_retry(text, path, voice, rate, retries, retry_delay)
            paths.append(path)
        segments.append(paths)
        print(f"generated {index}/{len(entries)}: {parts[0]}", flush=True)
    return segments


def combine_segments(segments, output, sentence_pause, entry_pause):
    sentence_silence = silence_mp3(sentence_pause)
    entry_silence = silence_mp3(entry_pause)

    with output.open("wb") as final:
        for segment in segments:
            for path in segment:
                final.write(path.read_bytes())
                final.write(sentence_silence)
            final.write(entry_silence)


def parse_args():
    parser = argparse.ArgumentParser(description="Generate bilingual MP3 from vocabulary JSON.")
    parser.add_argument("--input", required=True, help="Vocabulary JSON file.")
    parser.add_argument("--output", help="Output MP3 path.")
    parser.add_argument("--voice", default="en-US-EmmaMultilingualNeural", help="Multilingual TTS voice.")
    parser.add_argument("--rate", default="+0%", help="Speech rate, e.g. +0% or -5%.")
    parser.add_argument("--sentence-pause", type=float, default=0.5, help="Seconds after each sentence.")
    parser.add_argument("--entry-pause", type=float, default=0.0, help="Extra seconds after each vocabulary entry.")
    parser.add_argument("--limit", type=int, help="Generate only the first N words for preview.")
    parser.add_argument("--cache-dir", help="Directory for reusable TTS segments.")
    parser.add_argument("--retries", type=int, default=8, help="Retry attempts for each TTS segment.")
    parser.add_argument("--retry-delay", type=float, default=5.0, help="Base seconds between retries.")
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input)
    output = Path(args.output) if args.output else input_path.with_name(f"{input_path.stem}_bilingual.mp3")
    output.parent.mkdir(parents=True, exist_ok=True)

    entries = load_entries(input_path)
    if args.limit:
        entries = entries[:args.limit]

    cache_dir = Path(args.cache_dir) if args.cache_dir else Path(".cache") / "bilingual_audio_segments" / output.stem
    cache_dir.mkdir(parents=True, exist_ok=True)

    started = time.time()
    segments = asyncio.run(
        generate_segments(entries, args.voice, args.rate, cache_dir, args.retries, args.retry_delay)
    )
    combine_segments(segments, output, args.sentence_pause, args.entry_pause)

    audio = MP3(output)
    elapsed = time.time() - started
    print(
        f"{output} generated with {len(entries)} entries "
        f"({audio.info.length / 60:.2f} min, {output.stat().st_size / 1024 / 1024:.2f} MB, "
        f"{elapsed:.1f}s elapsed)."
    )


if __name__ == "__main__":
    main()
