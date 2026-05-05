#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


FIELDS = [
    "word",
    "wordTranslation",
    "phonetic",
    "partOfSpeech",
    "etymology",
    "example",
    "translation",
]


def load_payload(input_path):
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return {}, payload
    if isinstance(payload, dict) and isinstance(payload.get("words"), list):
        return payload, payload["words"]
    raise ValueError("Input must be a JSON array or an object with a words array.")


def validate_words(words):
    if not words:
        raise ValueError("words must not be empty.")

    errors = []
    for index, word in enumerate(words, start=1):
        missing = [field for field in FIELDS if field not in word]
        empty = [field for field in FIELDS if field in word and not str(word[field]).strip()]
        if missing:
            errors.append(f"#{index}: missing fields: {', '.join(missing)}")
        if empty:
            errors.append(f"#{index}: empty fields: {', '.join(empty)}")
    if errors:
        raise ValueError("\n".join(errors))


def escape_markdown(value):
    return str(value).replace("\n", " ").strip()


def render_markdown(meta, words, title):
    lines = [
        f"# {title}",
        "",
        f"共 {len(words)} 个词条。",
        "",
    ]

    for index, item in enumerate(words, start=1):
        word = escape_markdown(item["word"])
        phonetic = escape_markdown(item["phonetic"])
        lines.extend([
            f"## {index}. {word} {phonetic}",
            "",
            f"- 词性：{escape_markdown(item['partOfSpeech'])}",
            f"- 中文：{escape_markdown(item['wordTranslation'])}",
            f"- 词根：{escape_markdown(item['etymology'])}",
            f"- 例句：{escape_markdown(item['example'])}",
            f"- 翻译：{escape_markdown(item['translation'])}",
            "",
        ])

    return "\n".join(lines)


def parse_args():
    parser = argparse.ArgumentParser(description="Generate Markdown text from vocabulary JSON.")
    parser.add_argument("--input", required=True, help="Vocabulary JSON file.")
    parser.add_argument("--output", help="Output Markdown path. Defaults to input basename + .md.")
    parser.add_argument("--title", help="Markdown title. Defaults to deckName or input basename.")
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input)
    meta, words = load_payload(input_path)
    validate_words(words)

    output_path = Path(args.output) if args.output else input_path.with_suffix(".md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    title = args.title or meta.get("deckName") or input_path.stem.replace("_", " ").title()

    output_path.write_text(render_markdown(meta, words, title), encoding="utf-8")
    print(f"{output_path} generated with {len(words)} words.")


if __name__ == "__main__":
    main()
