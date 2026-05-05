---
name: anki-audio-deck
description: Use this skill when the user wants to turn an Anki vocabulary JSON word list into one MP3 audio file that reads each English word and its example sentence in standard American English pronunciation, with pauses between word, example, and the next card.
---

# Anki Audio Deck

Create one MP3 audio file for a vocabulary deck. The output filename should match the vocabulary JSON filename unless the user asks for another name. Keep each deck in its own directory:

```text
outputs/<deck_slug>/<deck_slug>.json
outputs/<deck_slug>/<deck_slug>.md
outputs/<deck_slug>/<deck_slug>.apkg
outputs/<deck_slug>/<deck_slug>.mp3
```

## Input

Use the same JSON shape as `create-anki-dictionary`:

- a list of word objects, or
- an object with a `words` array

Only these fields are required for audio:

- `word`
- `example`

## Generate

Use the bundled script:

```bash
python3 anki-audio-deck/scripts/generate_audio.py --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

Defaults:

- voice: `en-US-JennyNeural`
- word to example pause: `1` second
- next card pause: `2` seconds
- output: same basename and directory as input, with `.mp3`
- reusable TTS segments: `.cache/audio_segments/<deck_slug>/`

Useful options:

```bash
python3 anki-audio-deck/scripts/generate_audio.py --input outputs/interview_vocabulary/interview_vocabulary.json --word-pause 1 --card-pause 2
```

## Quality

- Use a standard US English voice.
- Read the word first, then its example sentence.
- Generate separate TTS segments and join MP3 bytes with generated silence so pauses are explicit.
- Keep text English-only in the generated audio.
- Validate the output file exists and is non-empty.
