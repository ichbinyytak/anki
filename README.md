# Anki Dictionary Deck Generator

一个用于生成 Anki 字典卡组的 Python 工具，支持词根词缀解析、音标、例句翻译和 TTS 自动播放。

## 卡片结构

### 正面
- 英文单词
- 音标
- 英文例句
- 播放按钮（TTS 朗读单词和例句）

### 背面
- 英文单词
- 音标
- 词性
- 词根词缀解析
- 单词中文翻译
- 英文例句
- 例句中文翻译
- 播放按钮

## 文件说明

| 文件 | 说明 |
|------|------|
| `create_anki_deck.py` | 主生成脚本，包含 10 个示例单词 |
| `template.py` | 通用模板，可用于生成其他单词卡组 |
| `dictionary_deck.apkg` | 生成的 Anki 卡组文件 |
| `SKILL.md` | Skill 说明文档 |

## 依赖

- Python 3
- genanki

```bash
pip install genanki
```

## 使用方法

### 1. 修改单词数据

编辑 `create_anki_deck.py` 中的 `words` 列表：

```python
words = [
    {
        'word': 'abandon',
        'wordTranslation': '放弃',
        'phonetic': '/əˈbændən/',
        'partOfSpeech': 'v.',
        'etymology': 'ab-离开 + band-捆绑',
        'example': 'He had to abandon his dream.',
        'translation': '他不得不放弃他的梦想。'
    },
    # 添加更多单词...
]
```

### 2. 生成卡组

```bash
python3 create_anki_deck.py
```

### 3. 导入 Anki

1. 打开 Anki / AnkiDroid
2. 导入 `dictionary_deck.apkg`
3. 开始学习

## TTS 设置

卡组使用 Anki 官方 TTS 标签，自动调用系统语音朗读。

### AnkiDroid 用户

1. 首次学习时会提示选择 TTS 语言，选择 **English (US)**
2. 或进入 **设置 → 高级 → 文本转语音** 配置

### 播放按钮

点击播放按钮可重新朗读单词和例句。

## 示例单词

| 单词 | 音标 | 词根 | 翻译 |
|------|------|------|------|
| abandon | /əˈbændən/ | ab-离开 + band-捆绑 | 放弃 |
| benevolent | /bɪˈnevələnt/ | bene-好 + vol-意愿 | 仁慈的 |
| comprehend | /ˌkɒmprɪˈhend/ | com-完全 + hend-抓住 | 理解 |
| contradict | /ˌkɒntrəˈdɪkt/ | contra-反 + dict-说 | 反驳 |
| enthusiastic | /ɪnˌθjuːziˈæstɪk/ | en-进入 + thus-神 | 热情的 |

## License

MIT
