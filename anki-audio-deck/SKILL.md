---
name: anki-audio-deck
description: "Use this skill when the user wants to turn an Anki vocabulary JSON word list into MP3 audio files: one English-only file that reads each English word and example sentence, and one bilingual English-Chinese file that also reads Chinese translations. Both versions use 0.5 second pauses by default."
---

# Anki Audio Deck

Create two MP3 audio files for a vocabulary deck by default: an English-only file and a bilingual English-Chinese file. Keep each deck in its own directory:

```text
outputs/<deck_slug>/<deck_slug>.json
outputs/<deck_slug>/<deck_slug>.md
outputs/<deck_slug>/<deck_slug>.apkg
outputs/<deck_slug>/<deck_slug>.mp3
outputs/<deck_slug>/<deck_slug>_bilingual.mp3
```

## Input

Use the same JSON shape as `create-anki-dictionary`:

- a list of word objects, or
- an object with a `words` array

Fields required for English-only audio:

- `word`
- `example`

Fields required for bilingual audio:

- `word`
- `wordTranslation`
- `example`
- `translation`

## Generate

Use the bundled scripts:

```bash
python3 anki-audio-deck/scripts/generate_audio.py --input outputs/immigration_vocabulary/immigration_vocabulary.json
python3 scripts/generate_bilingual_audio.py --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

English-only defaults:

- voice: `en-US-JennyNeural`
- word to example pause: `0.5` second
- next card pause: `0.5` second
- output: same basename and directory as input, with `.mp3`
- reusable TTS segments: `.cache/audio_segments/<deck_slug>/`

Bilingual defaults:

- voice: `en-US-EmmaMultilingualNeural`
- sentence pause: `0.5` second
- output: same basename and directory as input, with `_bilingual.mp3`
- reusable TTS segments: `.cache/bilingual_audio_segments/<deck_slug>_bilingual/`

Useful full build command:

```bash
python3 scripts/build_vocabulary.py --input outputs/interview_vocabulary/interview_vocabulary.json
```

## Quality

- Use a standard US English voice.
- English-only audio reads the word first, then its example sentence.
- Bilingual audio reads English word, Chinese word translation, English example, then Chinese example translation.
- Generate separate TTS segments and join MP3 bytes with generated silence so pauses are explicit.
- Validate both output files exist and are non-empty.
