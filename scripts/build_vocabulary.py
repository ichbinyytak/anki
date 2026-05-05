#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


def run(command):
    print(" ".join(command), flush=True)
    subprocess.run(command, check=True)


def parse_args():
    parser = argparse.ArgumentParser(description="Generate Markdown, APKG, English MP3, and bilingual MP3 for one vocabulary JSON.")
    parser.add_argument("--input", required=True, help="Path to outputs/<deck>/<deck>.json.")
    parser.add_argument("--word-pause", default="0.5", help="Seconds between word and example in English audio.")
    parser.add_argument("--card-pause", default="0.5", help="Seconds between cards in English audio.")
    parser.add_argument("--sentence-pause", default="0.5", help="Seconds after each sentence in bilingual audio.")
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")

    repo_root = Path(__file__).resolve().parents[1]
    text_script = repo_root / "scripts" / "generate_text.py"
    deck_script = repo_root / "scripts" / "generate_deck.py"
    audio_script = repo_root / "anki-audio-deck" / "scripts" / "generate_audio.py"
    bilingual_audio_script = repo_root / "scripts" / "generate_bilingual_audio.py"
    cache_dir = repo_root / ".cache" / "audio_segments" / input_path.stem
    bilingual_cache_dir = repo_root / ".cache" / "bilingual_audio_segments" / f"{input_path.stem}_bilingual"

    run([sys.executable, str(text_script), "--input", str(input_path)])
    run([sys.executable, str(deck_script), "--input", str(input_path)])
    run([
        sys.executable,
        str(audio_script),
        "--input",
        str(input_path),
        "--cache-dir",
        str(cache_dir),
        "--word-pause",
        args.word_pause,
        "--card-pause",
        args.card_pause,
    ])
    run([
        sys.executable,
        str(bilingual_audio_script),
        "--input",
        str(input_path),
        "--cache-dir",
        str(bilingual_cache_dir),
        "--sentence-pause",
        args.sentence_pause,
    ])


if __name__ == "__main__":
    main()
