import genanki

my_model = genanki.Model(
    1234567890,
    'Dictionary Model',
    fields=[
        {'name': 'Word'},
        {'name': 'WordTranslation'},
        {'name': 'Phonetic'},
        {'name': 'PartOfSpeech'},
        {'name': 'Etymology'},
        {'name': 'Example'},
        {'name': 'Translation'},
    ],
    templates=[
        {
            'name': 'Dictionary Card',
            'qfmt': '''
<div class="front">
    <div class="word">{{Word}}</div>
    <div class="phonetic">{{Phonetic}}</div>
    <div class="example">{{Example}}</div>
    <div class="play-btn">[anki:tts lang=en_US]{{Word}}. {{Example}}[/anki:tts]</div>
</div>
''',
            'afmt': '''
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
''',
        }
    ],
    css='''
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
'''
)

deck = genanki.Deck(9876543210, 'Dictionary Deck')

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
    {
        'word': 'benevolent',
        'wordTranslation': '仁慈的',
        'phonetic': '/bɪˈnevələnt/',
        'partOfSpeech': 'adj.',
        'etymology': 'bene-好 + vol-意愿',
        'example': 'The benevolent donor gave millions to charity.',
        'translation': '那位仁慈的捐赠者向慈善机构捐了数百万。'
    },
    {
        'word': 'comprehend',
        'wordTranslation': '理解',
        'phonetic': '/ˌkɒmprɪˈhend/',
        'partOfSpeech': 'v.',
        'etymology': 'com-完全 + pre-预先 + hend-抓住',
        'example': "I couldn't comprehend the complex theory.",
        'translation': '我无法理解这个复杂的理论。'
    },
    {
        'word': 'contradict',
        'wordTranslation': '反驳',
        'phonetic': '/ˌkɒntrəˈdɪkt/',
        'partOfSpeech': 'v.',
        'etymology': 'contra-反 + dict-说',
        'example': "The witness contradicted the defendant's statement.",
        'translation': '证人的陈述与被告的供词相矛盾。'
    },
    {
        'word': 'enthusiastic',
        'wordTranslation': '热情的',
        'phonetic': '/ɪnˌθjuːziˈæstɪk/',
        'partOfSpeech': 'adj.',
        'etymology': 'en-进入 + thus-神 + iast-疯狂的',
        'example': 'She was enthusiastic about the new project.',
        'translation': '她对这个新项目充满热情。'
    },
    {
        'word': 'magnificent',
        'wordTranslation': '壮丽的',
        'phonetic': '/mæɡˈnɪfɪsnt/',
        'partOfSpeech': 'adj.',
        'etymology': 'magn-大 + fic-做',
        'example': 'The palace was magnificent.',
        'translation': '那座宫殿富丽堂皇。'
    },
    {
        'word': 'photograph',
        'wordTranslation': '拍照',
        'phonetic': '/ˈfəʊtəɡrɑːf/',
        'partOfSpeech': 'v.',
        'etymology': 'photo-光 + graph-写',
        'example': 'I want to photograph the beautiful sunset.',
        'translation': '我想拍摄那美丽的日落。'
    },
    {
        'word': 'transparent',
        'wordTranslation': '透明的',
        'phonetic': '/trænsˈpærənt/',
        'partOfSpeech': 'adj.',
        'etymology': 'trans-穿过 + par-出现',
        'example': 'The water was so transparent.',
        'translation': '那水清澈透明。'
    },
    {
        'word': 'unanimous',
        'wordTranslation': '一致的',
        'phonetic': '/juːˈnænɪməs/',
        'partOfSpeech': 'adj.',
        'etymology': 'un-一 + anim-心',
        'example': 'The decision was unanimous.',
        'translation': '那项决定获得全票通过。'
    },
    {
        'word': 'vocabulary',
        'wordTranslation': '词汇',
        'phonetic': '/vəˈkæbjʊləri/',
        'partOfSpeech': 'n.',
        'etymology': 'voc-声音 + abul-能够',
        'example': 'Reading helps expand your vocabulary.',
        'translation': '阅读有助于扩大词汇量。'
    },
]

for w in words:
    note = genanki.Note(
        model=my_model,
        fields=[w['word'], w['wordTranslation'], w['phonetic'], w['partOfSpeech'], w['etymology'], w['example'], w['translation']]
    )
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file('/workspace/dictionary_deck.apkg')
print('dictionary_deck.apkg 已生成！')

