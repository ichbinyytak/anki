---
name: create-anki-dictionary
description: Use this skill when the user wants to create or update an Anki .apkg vocabulary deck from English words, Chinese translations, phonetics, parts of speech, etymology/root notes, example sentences, and Chinese example translations. Use it for new themed decks such as immigration, daily life, fitness, interview, legal, or exam vocabulary.
---

# Create Anki Dictionary Deck

This skill creates Anki vocabulary decks with bilingual dictionary cards and English TTS.

## Workflow

1. Collect or create word data with these exact fields:
   `word`, `wordTranslation`, `phonetic`, `partOfSpeech`, `etymology`, `example`, `translation`.
2. Keep examples natural and practical for the deck theme. For immigration or legal topics, prefer neutral official-language examples over harsh or stigmatizing phrasing.
3. Save the data as JSON under a dedicated output folder:

```text
outputs/<deck_slug>/<deck_slug>.json
```

Use either a list of word objects or this object shape:

```json
{
  "deckName": "Immigration Vocabulary",
  "modelName": "Immigration Vocabulary Model",
  "words": [
    {
      "word": "visa",
      "wordTranslation": "签证",
      "phonetic": "/ˈviːzə/",
      "partOfSpeech": "n.",
      "etymology": "来自拉丁语 visa（被看过的）",
      "example": "You need a valid visa to enter the country.",
      "translation": "你需要有效签证才能进入该国。"
    }
  ]
}
```

4. Generate the deck with the bundled script:

```bash
python3 scripts/generate_deck.py --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

Optional overrides:

```bash
python3 scripts/generate_deck.py --input outputs/interview_vocabulary/interview_vocabulary.json --deck-name "Interview Vocabulary"
```

By default, the `.apkg` is written next to the input JSON with the same basename.

To generate both `.apkg` and `.mp3` for a completed deck directory, use:

```bash
python3 scripts/build_vocabulary.py --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

## Validation

Before finishing, run the generator and confirm it reports the expected word count. The script rejects:

- missing required fields
- empty field values
- duplicate words, case-insensitive
- invalid JSON shape

If `genanki` is missing, install dependencies from the repository root:

```bash
python3 -m pip install --user -r requirements.txt
```

## Card Format

Front:

- English word
- phonetic
- English example
- `[anki:tts lang=en_US]{{Word}}. {{Example}}[/anki:tts]`

Back:

- English word, phonetic, part of speech
- etymology/root note
- Chinese word translation
- English example and Chinese translation
- the same TTS control

## Quality Bar

- Each word should be useful for the requested theme, not just broadly related.
- Prefer one clear sense per card. If a word has multiple important senses, create separate phrase cards.
- Use conventional capitalization for abbreviations such as `USCIS`, `NVC`, `RFE`, and `NOA`.
- Keep Chinese translations concise, but make example translations complete and natural.
- Do not leave English placeholder text in Chinese fields.
