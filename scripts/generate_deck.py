#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import genanki

FIELDS = [
    "word",
    "wordTranslation",
    "phonetic",
    "partOfSpeech",
    "etymology",
    "example",
    "translation",
]


CARD_CSS = """
.card {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 20px;
    text-align: center;
    color: #333;
    background-color: #f5f5f5;
}
.front, .back {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.word {
    font-size: 36px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 5px;
}
.phonetic {
    font-size: 16px;
    color: #7f8c8d;
    margin-bottom: 15px;
}
.pos {
    font-size: 16px;
    color: #8e44ad;
    margin-bottom: 8px;
}
.etymology {
    font-size: 14px;
    color: #8e44ad;
    margin-bottom: 10px;
    padding: 10px 15px;
    background-color: #f5eef8;
    border-radius: 8px;
}
.word-trans {
    font-size: 18px;
    color: #e74c3c;
    margin-bottom: 15px;
}
.example {
    font-size: 16px;
    color: #34495e;
    font-style: italic;
    margin-bottom: 10px;
    padding: 15px;
    background-color: #ecf0f1;
    border-radius: 8px;
}
.translation {
    font-size: 16px;
    color: #27ae60;
    padding: 10px 0;
}
.play-btn {
    margin: 15px 0;
    padding: 12px 30px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    display: inline-block;
    font-size: 14px;
}
"""


def stable_id(value):
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) % 2_000_000_000 + 1


def slugify(value):
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "dictionary_deck"


def load_payload(input_path):
    if input_path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(input_path).read_text(encoding="utf-8")
    payload = json.loads(raw)
    if isinstance(payload, list):
        return {}, payload
    if isinstance(payload, dict) and isinstance(payload.get("words"), list):
        return payload, payload["words"]
    raise ValueError("Input must be a JSON array or an object with a words array.")


def validate_words(words):
    if not words:
        raise ValueError("words must not be empty.")

    seen = {}
    errors = []
    for index, word in enumerate(words, start=1):
        if not isinstance(word, dict):
            errors.append(f"#{index}: item must be an object")
            continue

        missing = [field for field in FIELDS if field not in word]
        if missing:
            errors.append(f"#{index}: missing fields: {', '.join(missing)}")
            continue

        empty = [field for field in FIELDS if not str(word[field]).strip()]
        if empty:
            errors.append(f"#{index} {word.get('word', '')}: empty fields: {', '.join(empty)}")

        key = str(word["word"]).strip().lower()
        if key in seen:
            errors.append(f"#{index} {word['word']}: duplicate of #{seen[key]}")
        else:
            seen[key] = index

    if errors:
        raise ValueError("\n".join(errors))


def create_model(model_name, model_id):
    return genanki.Model(
        model_id,
        model_name,
        fields=[
            {"name": "Word"},
            {"name": "WordTranslation"},
            {"name": "Phonetic"},
            {"name": "PartOfSpeech"},
            {"name": "Etymology"},
            {"name": "Example"},
            {"name": "Translation"},
        ],
        templates=[
            {
                "name": "Dictionary Card",
                "qfmt": """
<div class="front">
    <div class="word">{{Word}}</div>
    <div class="phonetic">{{Phonetic}}</div>
    <div class="example">{{Example}}</div>
    <div class="play-btn">[anki:tts lang=en_US]{{Word}}. {{Example}}[/anki:tts]</div>
</div>
""",
                "afmt": """
<div class="back">
    <div class="word">{{Word}}</div>
    <div class="phonetic">{{Phonetic}}</div>
    <div class="pos">{{PartOfSpeech}}</div>
    <div class="etymology">{{Etymology}}</div>
    <div class="word-trans">{{WordTranslation}}</div>
    <div class="example">{{Example}}</div>
    <div class="translation">{{Translation}}</div>
    <div class="play-btn">[anki:tts lang=en_US]{{Word}}. {{Example}}[/anki:tts]</div>
</div>
""",
            }
        ],
        css=CARD_CSS,
    )


def build_deck(words, deck_name, model_name):
    deck_id = stable_id(f"deck:{deck_name}")
    model_id = stable_id(f"model:{model_name}")
    model = create_model(model_name, model_id)
    deck = genanki.Deck(deck_id, deck_name)

    for word in words:
        note = genanki.Note(
            model=model,
            fields=[
                str(word["word"]).strip(),
                str(word["wordTranslation"]).strip(),
                str(word["phonetic"]).strip(),
                str(word["partOfSpeech"]).strip(),
                str(word["etymology"]).strip(),
                str(word["example"]).strip(),
                str(word["translation"]).strip(),
            ],
        )
        deck.add_note(note)

    return deck


def parse_args():
    parser = argparse.ArgumentParser(description="Generate an Anki dictionary deck from JSON.")
    parser.add_argument("--input", required=True, help="JSON file path, or '-' for stdin.")
    parser.add_argument("--deck-name", help="Anki deck name. Overrides deckName in JSON.")
    parser.add_argument("--model-name", help="Anki note model name.")
    parser.add_argument("--output", help="Output .apkg path.")
    return parser.parse_args()


def main():
    args = parse_args()
    meta, words = load_payload(args.input)
    deck_name = args.deck_name or meta.get("deckName") or "Dictionary Deck"
    model_name = args.model_name or meta.get("modelName") or f"{deck_name} Model"
    output = args.output or meta.get("output") or str(Path(args.input).with_suffix(".apkg"))

    validate_words(words)

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    package = genanki.Package(build_deck(words, deck_name, model_name))
    package.write_to_file(str(output_path))
    print(f"{output_path} generated with {len(words)} words.")


if __name__ == "__main__":
    main()
