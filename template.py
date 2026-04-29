import genanki
import json

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

words = []
for w in words:
    note = genanki.Note(
        model=my_model,
        fields=[w['word'], w['wordTranslation'], w['phonetic'], w['partOfSpeech'], w['etymology'], w['example'], w['translation']]
    )
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file('/workspace/dictionary_deck.apkg')
print('dictionary_deck.apkg 已生成！')
