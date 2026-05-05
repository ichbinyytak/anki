# Anki Vocabulary Skills

这个项目用于用 Codex skill 生成英语词库成品。核心原则是：**JSON 是唯一源文件**，文字版、Anki 卡组和跟读音频都从同一个 JSON 生成。

- `create-anki-dictionary`: 从 JSON 词库生成文字版 `.md` 和 Anki `.apkg`
- `anki-audio-deck`: 从同一个 JSON 词库生成跟读 `.mp3`

## 目录约定

每个词库一个独立目录，只放这个词库的最终成品：

```text
outputs/
  immigration_vocabulary/
    immigration_vocabulary.json
    immigration_vocabulary.md
    immigration_vocabulary.apkg
    immigration_vocabulary.mp3
    immigration_vocabulary_bilingual.mp3
```

临时语音片段缓存放在 `.cache/audio_segments/`，不放进词库成品目录。

## 现有词库

| 词库 | 词条数 | 目录 |
|------|--------|------|
| Dictionary Deck | 10 | `outputs/dictionary_deck/` |
| Daily Life Vocabulary | 150 | `outputs/daily_life_vocabulary/` |
| Fitness Vocabulary | 140 | `outputs/fitness_vocabulary/` |
| Immigration Vocabulary | 147 | `outputs/immigration_vocabulary/` |

## 词库 JSON

词库文件使用以下结构。`deckName` 和 `modelName` 必须为每个词库设置不同名称，否则 Anki 导入时可能和已有卡组冲突。

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

## 生成文字版

```bash
python3 scripts/generate_text.py \
  --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

默认输出：

```text
outputs/immigration_vocabulary/immigration_vocabulary.md
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

## 生成全英文跟读音频

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
- 单词后停顿 `0.5` 秒
- 例句后停顿 `0.5` 秒，再进入下一组

## 生成中英文跟读音频

如果需要把中文释义和例句翻译也读出来，可以生成双语版：

```bash
python3 scripts/generate_bilingual_audio.py \
  --input outputs/immigration_vocabulary/immigration_vocabulary.json
```

默认输出：

```text
outputs/immigration_vocabulary/immigration_vocabulary_bilingual.mp3
```

双语版会读取：英文单词、中文释义、英文例句、中文翻译。默认每句后停顿 `0.5` 秒，使用中英混读语音。

## 新增词库流程

1. 新建目录：`outputs/<deck_slug>/`
2. 保存词库：`outputs/<deck_slug>/<deck_slug>.json`
3. 运行一条命令生成 `.md`、`.apkg`、全英文 `.mp3` 和中英文 `_bilingual.mp3`

```bash
python3 scripts/build_vocabulary.py \
  --input outputs/<deck_slug>/<deck_slug>.json
```

生成顺序固定为：

```text
JSON -> Markdown -> APKG -> English MP3 -> Bilingual MP3
```

如果需要修改词条，只改 JSON，然后重新运行构建命令。

## Skill 文件

- [SKILL.md](SKILL.md): Anki 卡组生成 skill
- [anki-audio-deck/SKILL.md](anki-audio-deck/SKILL.md): MP3 跟读音频生成 skill

## 远程仓库

```bash
git remote add origin https://github.com/ichbinyytak/anki.git
git push origin master
```
