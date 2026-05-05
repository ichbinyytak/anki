# Anki Vocabulary Skills

这个项目用于用 Codex skill 生成英语词库成品：

- `create-anki-dictionary`: 从 JSON 词库生成 Anki `.apkg`
- `anki-audio-deck`: 从同一个 JSON 词库生成跟读 `.mp3`

## 目录约定

每个词库一个独立目录，只放这个词库的最终成品：

```text
outputs/
  immigration_vocabulary/
    immigration_vocabulary.json
    immigration_vocabulary.apkg
    immigration_vocabulary.mp3
```

临时语音片段缓存放在 `.cache/audio_segments/`，不放进词库成品目录。

## 词库 JSON

词库文件使用以下结构：

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

## 安装依赖

```bash
python3 -m pip install --user -r requirements.txt
```

## 生成 Anki 卡组

```bash
python3 scripts/generate_deck.py \
  --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

默认输出：

```text
outputs/immigration_vocabulary/immigration_vocabulary.apkg
```

## 生成跟读音频

```bash
python3 anki-audio-deck/scripts/generate_audio.py \
  --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

默认输出：

```text
outputs/immigration_vocabulary/immigration_vocabulary.mp3
```

音频规则：

- 标准美式发音，默认 `en-US-JennyNeural`
- 单词后停顿 `1` 秒
- 例句后停顿 `2` 秒，再进入下一组

## 新增词库流程

1. 新建目录：`outputs/<deck_slug>/`
2. 保存词库：`outputs/<deck_slug>/<deck_slug>.json`
3. 运行一条命令生成 `.apkg` 和 `.mp3`

```bash
python3 scripts/build_vocabulary.py \
  --input outputs/<deck_slug>/<deck_slug>.json
```

## Skill 文件

- [SKILL.md](SKILL.md): Anki 卡组生成 skill
- [anki-audio-deck/SKILL.md](anki-audio-deck/SKILL.md): MP3 跟读音频生成 skill
