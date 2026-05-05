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


def load_words(input_path):
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    if isinstance(payload, list):
        words = payload
    elif isinstance(payload, dict) and isinstance(payload.get("words"), list):
        words = payload["words"]
    else:
        raise ValueError("Input must be a JSON array or an object with a words array.")

    cleaned = []
    for index, item in enumerate(words, start=1):
        word = str(item.get("word", "")).strip()
        example = str(item.get("example", "")).strip()
        if not word or not example:
            raise ValueError(f"Item #{index} must include non-empty word and example fields.")
        cleaned.append((word, example))
    return cleaned


def silence_mp3(seconds, sample_rate=24000, channels=1, bit_rate=64):
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(bit_rate)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)

    sample_count = int(sample_rate * seconds)
    pcm = b"\x00\x00" * sample_count * channels
    return encoder.encode(pcm) + encoder.flush()


def cache_name(index, kind, text, voice):
    digest = hashlib.sha256(f"{voice}\0{text}".encode("utf-8")).hexdigest()[:16]
    return f"{index:04d}_{kind}_{digest}.mp3"


async def generate_audio(text, voice, output):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output)


async def generate_audio_with_retry(text, voice, output, retries, retry_delay):
    output_path = Path(output)
    if output_path.exists() and output_path.stat().st_size > 0:
        return

    last_error = None
    for attempt in range(1, retries + 1):
        try:
            await generate_audio(text, voice, str(output_path))
            if output_path.stat().st_size == 0:
                raise RuntimeError(f"{output_path} is empty")
            return
        except Exception as error:
            last_error = error
            output_path.unlink(missing_ok=True)
            if attempt == retries:
                break
            sleep_for = retry_delay * attempt + random.uniform(0, 1.5)
            print(f"retry {attempt}/{retries} after TTS error: {error}", flush=True)
            await asyncio.sleep(sleep_for)

    raise RuntimeError(f"failed to generate {output_path}: {last_error}")


async def generate_segments(words, voice, cache_dir, retries, retry_delay):
    paths = []
    for index, (word, example) in enumerate(words, start=1):
        word_path = cache_dir / cache_name(index, "word", word, voice)
        example_path = cache_dir / cache_name(index, "example", example, voice)
        await generate_audio_with_retry(word, voice, word_path, retries, retry_delay)
        await generate_audio_with_retry(example, voice, example_path, retries, retry_delay)
        paths.append((word_path, example_path))
        print(f"generated {index}/{len(words)}: {word}", flush=True)
    return paths


def combine_segments(segments, output, word_pause, card_pause):
    word_silence = silence_mp3(word_pause)
    card_silence = silence_mp3(card_pause)

    with Path(output).open("wb") as out:
        for word_path, example_path in segments:
            out.write(word_path.read_bytes())
            out.write(word_silence)
            out.write(example_path.read_bytes())
            out.write(card_silence)


def parse_args():
    parser = argparse.ArgumentParser(description="Generate MP3 audio from Anki vocabulary JSON.")
    parser.add_argument("--input", required=True, help="Vocabulary JSON file.")
    parser.add_argument("--output", help="Output MP3 path. Defaults to input basename + .mp3.")
    parser.add_argument("--voice", default="en-US-JennyNeural", help="edge-tts US English voice.")
    parser.add_argument("--word-pause", type=float, default=1.0, help="Seconds between word and example.")
    parser.add_argument("--card-pause", type=float, default=2.0, help="Seconds between cards.")
    parser.add_argument("--limit", type=int, help="Generate only the first N words for preview.")
    parser.add_argument("--cache-dir", help="Directory for reusable TTS segments.")
    parser.add_argument("--retries", type=int, default=8, help="Retry attempts for each TTS segment.")
    parser.add_argument("--retry-delay", type=float, default=5.0, help="Base seconds between retries.")
    return parser.parse_args()


def main():
    args = parse_args()
    words = load_words(args.input)
    if args.limit:
        words = words[:args.limit]

    output = Path(args.output) if args.output else Path(args.input).with_suffix(".mp3")
    output.parent.mkdir(parents=True, exist_ok=True)

    cache_dir = Path(args.cache_dir) if args.cache_dir else Path(".cache") / "audio_segments" / output.stem
    cache_dir.mkdir(parents=True, exist_ok=True)

    started = time.time()
    segments = asyncio.run(
        generate_segments(words, args.voice, cache_dir, args.retries, args.retry_delay)
    )
    combine_segments(segments, output, args.word_pause, args.card_pause)

    duration = MP3(output).info.length
    elapsed = time.time() - started
    print(f"{output} generated with {len(words)} word/example pairs ({duration:.1f}s, {elapsed:.1f}s elapsed).")


if __name__ == "__main__":
    main()
