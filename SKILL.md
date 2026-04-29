---
name: create-anki-dictionary
description: 根据提供的单词列表生成 Anki 字典卡组.apkg文件。支持词根词缀解析、音标、例句翻译。使用 genanki 库生成。
arguments:
  - name: words
    description: 单词数据，格式为JSON数组。每个单词包含 word(英文), wordTranslation(中文), phonetic(音标), partOfSpeech(词性), etymology(词根), example(例句), translation(例句翻译)
    required: true
---

# 创建 Anki 字典卡组

根据用户提供的单词列表，生成 Anki 字典卡组 `.apkg` 文件。

## 输入格式

用户提供 JSON 格式的单词数组，每个单词包含：
- `word`: 英文单词
- `wordTranslation`: 单词中文翻译
- `phonetic`: 音标
- `partOfSpeech`: 词性（如 v., adj., n.）
- `etymology`: 词根词缀解析
- `example`: 英文例句
- `translation`: 例句中文翻译

## 生成脚本

使用 genanki 库生成卡组，模板结构：

**正面**：
- 单词
- 音标
- 英文例句
- 播放按钮（TTS 同时播放单词和例句）

**背面**：
- 单词
- 音标
- 词性
- 词根
- 单词翻译
- 英文例句
- 例句翻译
- 播放按钮

## 执行步骤

1. **准备数据**：解析用户提供的单词列表
2. **创建脚本**：生成 Python 脚本调用 genanki
3. **生成文件**：执行脚本生成 `.apkg` 文件
4. **输出结果**：告知用户文件位置

## 模板样式

```css
- 卡片背景：白色，圆角 10px，阴影
- 单词：36px，深蓝色粗体
- 音标：16px，灰色
- 词性：16px，紫色
- 词根：14px，紫色背景
- 单词翻译：18px，红色
- 例句：16px，斜体，浅灰背景
- 翻译：16px，绿色
- 播放按钮：蓝色，25px 圆角
```

## TTS 语法

使用 Anki 官方 TTS 标签：
```
[anki:tts lang=en_US]{{Word}}. {{Example}}[/anki:tts]
```

## 示例单词数据

```json
[
  {
    "word": "abandon",
    "wordTranslation": "放弃",
    "phonetic": "/əˈbændən/",
    "partOfSpeech": "v.",
    "etymology": "ab-离开 + band-捆绑",
    "example": "He had to abandon his dream.",
    "translation": "他不得不放弃他的梦想。"
  }
]
```

## 依赖

- Python 3
- genanki 库：`pip install genanki`

## 输出

生成的 `.apkg` 文件保存在 `/workspace/dictionary_deck.apkg`
