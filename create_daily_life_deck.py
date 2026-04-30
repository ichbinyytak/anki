import genanki

my_model = genanki.Model(
    1234567890,
    'Daily Life Dictionary Model',
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

deck = genanki.Deck(9876543212, 'Daily Life Vocabulary')

words = [
    # 家庭
    {"word": "family", "wordTranslation": "家庭/家人", "phonetic": "/ˈfæməli/", "partOfSpeech": "n.", "etymology": "fam-家庭 + -ly", "example": "My family is important.", "translation": "我的家庭很重要。"},
    {"word": "home", "wordTranslation": "家", "phonetic": "/həʊm/", "partOfSpeech": "n.", "etymology": "来自古英语ham", "example": "Welcome home.", "translation": "欢迎回家。"},
    {"word": "house", "wordTranslation": "房子", "phonetic": "/haʊs/", "partOfSpeech": "n.", "etymology": "来自古英语hus", "example": "Buy a new house.", "translation": "买新房子。"},
    {"word": "apartment", "wordTranslation": "公寓", "phonetic": "/əˈpɑːtmənt/", "partOfSpeech": "n.", "etymology": "apart-分开 + -ment", "example": "Rent an apartment.", "translation": "租公寓。"},
    {"word": "room", "wordTranslation": "房间", "phonetic": "/ruːm/", "partOfSpeech": "n.", "etymology": "来自古英语rum", "example": "Clean your room.", "translation": "打扫你的房间。"},
    {"word": "kitchen", "wordTranslation": "厨房", "phonetic": "/ˈkɪtʃɪn/", "partOfSpeech": "n.", "etymology": "cook-烹饪 + -en", "example": "Cook in the kitchen.", "translation": "在厨房做饭。"},
    {"word": "bedroom", "wordTranslation": "卧室", "phonetic": "/ˈbedruːm/", "partOfSpeech": "n.", "etymology": "bed-床 + room-房间", "example": "Go to the bedroom.", "translation": "去卧室。"},
    {"word": "bathroom", "wordTranslation": "浴室/洗手间", "phonetic": "/ˈbɑːθruːm/", "partOfSpeech": "n.", "etymology": "bath-沐浴 + room-房间", "example": "Use the bathroom.", "translation": "用洗手间。"},
    {"word": "living room", "wordTranslation": "客厅", "phonetic": "/ˈlɪvɪŋ ruːm/", "partOfSpeech": "n.", "etymology": "living-生活的 + room-房间", "example": "Watch TV in the living room.", "translation": "在客厅看电视。"},
    {"word": "garden", "wordTranslation": "花园", "phonetic": "/ˈɡɑːdən/", "partOfSpeech": "n.", "etymology": "来自古英语geard", "example": "Work in the garden.", "translation": "在花园干活。"},

    # 家人
    {"word": "mother", "wordTranslation": "妈妈", "phonetic": "/ˈmʌðər/", "partOfSpeech": "n.", "etymology": "来自古英语modor", "example": "Call your mother.", "translation": "给你妈妈打电话。"},
    {"word": "father", "wordTranslation": "爸爸", "phonetic": "/ˈfɑːðər/", "partOfSpeech": "n.", "etymology": "来自古英语fæder", "example": "My father is tall.", "translation": "我爸爸很高。"},
    {"word": "parent", "wordTranslation": "父母", "phonetic": "/ˈpeərənt/", "partOfSpeech": "n.", "etymology": "par-生产 + -ent", "example": "Live with parents.", "translation": "和父母住一起。"},
    {"word": "brother", "wordTranslation": "兄弟", "phonetic": "/ˈbrʌðər/", "partOfSpeech": "n.", "etymology": "来自古英语brodor", "example": "My brother is older.", "translation": "我哥哥更大。"},
    {"word": "sister", "wordTranslation": "姐妹", "phonetic": "/ˈsɪstər/", "partOfSpeech": "n.", "etymology": "来自古英语sweostor", "example": "I have a sister.", "translation": "我有一个姐姐。"},
    {"word": "son", "wordTranslation": "儿子", "phonetic": "/sʌn/", "partOfSpeech": "n.", "etymology": "来自古英语sunu", "example": "My son is clever.", "translation": "我儿子很聪明。"},
    {"word": "daughter", "wordTranslation": "女儿", "phonetic": "/ˈdɔːtər/", "partOfSpeech": "n.", "etymology": "来自古英语dohtor", "example": "Her daughter is cute.", "translation": "她女儿很可爱。"},
    {"word": "child", "wordTranslation": "孩子", "phonetic": "/tʃaɪld/", "partOfSpeech": "n.", "etymology": "来自古英语cild", "example": "Take care of the child.", "translation": "照顾孩子。"},
    {"word": "children", "wordTranslation": "孩子们", "phonetic": "/ˈtʃɪldrən/", "partOfSpeech": "n.", "etymology": "child-孩子 + -ren复数", "example": "The children are playing.", "translation": "孩子们在玩。"},
    {"word": "grandmother", "wordTranslation": "奶奶/外婆", "phonetic": "/ˈɡrænmʌðər/", "partOfSpeech": "n.", "etymology": "grand-大 + mother-母亲", "example": "Visit grandmother.", "translation": "去看奶奶。"},

    # 食物和饮料
    {"word": "food", "wordTranslation": "食物", "phonetic": "/fuːd/", "partOfSpeech": "n.", "etymology": "来自古英语foda", "example": "Buy some food.", "translation": "买些食物。"},
    {"word": "water", "wordTranslation": "水", "phonetic": "/ˈwɔːtər/", "partOfSpeech": "n.", "etymology": "来自古英语wæter", "example": "Drink water.", "translation": "喝水。"},
    {"word": "milk", "wordTranslation": "牛奶", "phonetic": "/mɪlk/", "partOfSpeech": "n.", "etymology": "来自古英语meolc", "example": "Buy a gallon of milk.", "translation": "买一加仑牛奶。"},
    {"word": "coffee", "wordTranslation": "咖啡", "phonetic": "/ˈkɒfi/", "partOfSpeech": "n.", "etymology": "来自阿拉伯语qahwah", "example": "I drink coffee every morning.", "translation": "我每天早上喝咖啡。"},
    {"word": "tea", "wordTranslation": "茶", "phonetic": "/tiː/", "partOfSpeech": "n.", "etymology": "来自汉语te", "example": "Make some tea.", "translation": "泡杯茶。"},
    {"word": "bread", "wordTranslation": "面包", "phonetic": "/bred/", "partOfSpeech": "n.", "etymology": "来自古英语beorm", "example": "Toast the bread.", "translation": "烤面包。"},
    {"word": "rice", "wordTranslation": "米饭", "phonetic": "/raɪs/", "partOfSpeech": "n.", "etymology": "来自古法语ris", "example": "Cook rice.", "translation": "煮米饭。"},
    {"word": "meat", "wordTranslation": "肉", "phonetic": "/miːt/", "partOfSpeech": "n.", "etymology": "来自古英语mete", "example": "Eat less meat.", "translation": "少吃肉。"},
    {"word": "vegetable", "wordTranslation": "蔬菜", "phonetic": "/ˈvedʒtəbəl/", "partOfSpeech": "n.", "etymology": "veget-生长 + -able", "example": "Eat more vegetables.", "translation": "多吃蔬菜。"},
    {"word": "fruit", "wordTranslation": "水果", "phonetic": "/fruːt/", "partOfSpeech": "n.", "etymology": "来自拉丁语fructus", "example": "Fresh fruit is healthy.", "translation": "新鲜水果健康。"},

    # 餐饮
    {"word": "breakfast", "wordTranslation": "早餐", "phonetic": "/ˈbrekfəst/", "partOfSpeech": "n.", "etymology": "break-打破 + fast-禁食", "example": "Have breakfast at 8.", "translation": "8点吃早餐。"},
    {"word": "lunch", "wordTranslation": "午餐", "phonetic": "/lʌntʃ/", "partOfSpeech": "n.", "etymology": "来自古英语nuncheon", "example": "Let's have lunch.", "translation": "我们吃午饭吧。"},
    {"word": "dinner", "wordTranslation": "晚餐", "phonetic": "/ˈdɪnər/", "partOfSpeech": "n.", "etymology": "来自古法语disner", "example": "Dinner is ready.", "translation": "晚饭好了。"},
    {"word": "restaurant", "wordTranslation": "餐厅", "phonetic": "/ˈrestərɒnt/", "partOfSpeech": "n.", "etymology": "rest-休息 + aurant-金箔匠", "example": "Book a restaurant.", "translation": "预订餐厅。"},
    {"word": "menu", "wordTranslation": "菜单", "phonetic": "/ˈmenjuː/", "partOfSpeech": "n.", "etymology": "来自法语menu（小的）", "example": "Check the menu.", "translation": "查看菜单。"},
    {"word": "recipe", "wordTranslation": "食谱", "phonetic": "/ˈresɪpi/", "partOfSpeech": "n.", "etymology": "re-再 + cip-拿 + -e", "example": "Follow this recipe.", "translation": "按照这个食谱做。"},
    {"word": "ingredient", "wordTranslation": "原料", "phonetic": "/ɪnˈɡriːdiənt/", "partOfSpeech": "n.", "etymology": "in-内 + gred-步 + -ient", "example": "Buy ingredients.", "translation": "买原料。"},
    {"word": "delicious", "wordTranslation": "美味的", "phonetic": "/dɪˈlɪʃəs/", "partOfSpeech": "adj.", "etymology": "de-完全 + lic-诱惑 + -ious", "example": "This food is delicious.", "translation": "这食物很美味。"},
    {"word": "hungry", "wordTranslation": "饿的", "phonetic": "/ˈhʌŋɡri/", "partOfSpeech": "adj.", "etymology": "hung-挂 + -ry", "example": "I'm hungry.", "translation": "我饿了。"},
    {"word": "thirsty", "wordTranslation": "渴的", "phonetic": "/ˈθɜːsti/", "partOfSpeech": "adj.", "etymology": "thirst-渴 + -y", "example": "I'm thirsty.", "translation": "我渴了。"},

    # 购物
    {"word": "shop", "wordTranslation": "商店", "phonetic": "/ʃɒp/", "partOfSpeech": "n.", "etymology": "来自古英语scoop", "example": "Go to the shop.", "translation": "去商店。"},
    {"word": "store", "wordTranslation": "店铺", "phonetic": "/stɔːr/", "partOfSpeech": "n.", "etymology": "来自古英语stoor", "example": "Open the store.", "translation": "开店。"},
    {"word": "supermarket", "wordTranslation": "超市", "phonetic": "/ˈsuːpəmɑːkɪt/", "partOfSpeech": "n.", "etymology": "super-超级 + market-市场", "example": "Buy groceries at supermarket.", "translation": "在超市买杂货。"},
    {"word": "price", "wordTranslation": "价格", "phonetic": "/praɪs/", "partOfSpeech": "n.", "etymology": "来自拉丁语pretium", "example": "What's the price?", "translation": "价格是多少？"},
    {"word": "cheap", "wordTranslation": "便宜的", "phonetic": "/tʃiːp/", "partOfSpeech": "adj.", "etymology": "来自古英语ceap", "example": "It's very cheap.", "translation": "很便宜。"},
    {"word": "expensive", "wordTranslation": "贵的", "phonetic": "/ɪkˈspensɪv/", "partOfSpeech": "adj.", "etymology": "ex-出 + pens-花费 + -ive", "example": "That's too expensive.", "translation": "那太贵了。"},
    {"word": "discount", "wordTranslation": "折扣", "phonetic": "/ˈdɪskaʊnt/", "partOfSpeech": "n.", "etymology": "dis-不 + count-计算", "example": "Get a discount.", "translation": "获得折扣。"},
    {"word": "buy", "wordTranslation": "买", "phonetic": "/baɪ/", "partOfSpeech": "v.", "etymology": "来自古英语bycgan", "example": "I want to buy this.", "translation": "我想买这个。"},
    {"word": "sell", "wordTranslation": "卖", "phonetic": "/sel/", "partOfSpeech": "v.", "etymology": "来自古英语sellan", "example": "Sell your car.", "translation": "卖你的车。"},
    {"word": "pay", "wordTranslation": "支付", "phonetic": "/peɪ/", "partOfSpeech": "v.", "etymology": "来自拉丁语pac", "example": "Pay by card.", "translation": "用卡支付。"},

    # 交通
    {"word": "car", "wordTranslation": "汽车", "phonetic": "/kɑːr/", "partOfSpeech": "n.", "etymology": "来自拉丁语carrus", "example": "Drive the car.", "translation": "开车。"},
    {"word": "bus", "wordTranslation": "公交车", "phonetic": "/bʌs/", "partOfSpeech": "n.", "etymology": "omnibus的缩写", "example": "Take the bus.", "translation": "坐公交车。"},
    {"word": "train", "wordTranslation": "火车", "phonetic": "/treɪn/", "partOfSpeech": "n.", "etymology": "来自古法语trainer", "example": "Catch the train.", "translation": "赶火车。"},
    {"word": "subway", "wordTranslation": "地铁", "phonetic": "/ˈsʌbweɪ/", "partOfSpeech": "n.", "etymology": "sub-下 + way-路", "example": "Take the subway.", "translation": "坐地铁。"},
    {"word": "taxi", "wordTranslation": "出租车", "phonetic": "/ˈtæksi/", "partOfSpeech": "n.", "etymology": "taximeter的缩写", "example": "Call a taxi.", "translation": "叫出租车。"},
    {"word": "bicycle", "wordTranslation": "自行车", "phonetic": "/ˈbaɪsɪkəl/", "partOfSpeech": "n.", "etymology": "bi-二 + cycl-圆 + -e", "example": "Ride a bicycle.", "translation": "骑自行车。"},
    {"word": "airplane", "wordTranslation": "飞机", "phonetic": "/ˈeərpleɪn/", "partOfSpeech": "n.", "etymology": "air-空气 + plane-平面", "example": "Take an airplane.", "translation": "坐飞机。"},
    {"word": "ticket", "wordTranslation": "票", "phonetic": "/ˈtɪkɪt/", "partOfSpeech": "n.", "etymology": "来自古法语estiquet", "example": "Buy a ticket.", "translation": "买票。"},
    {"word": "station", "wordTranslation": "车站", "phonetic": "/ˈsteɪʃən/", "partOfSpeech": "n.", "etymology": "stat-站立 + -ion", "example": "Go to the station.", "translation": "去车站。"},
    {"word": "driver", "wordTranslation": "司机", "phonetic": "/ˈdraɪvər/", "partOfSpeech": "n.", "etymology": "driv-驾驶 + -er", "example": "The driver is waiting.", "translation": "司机在等。"},

    # 时间
    {"word": "time", "wordTranslation": "时间", "phonetic": "/taɪm/", "partOfSpeech": "n.", "etymology": "来自古英语tima", "example": "What time is it?", "translation": "现在几点了？"},
    {"word": "today", "wordTranslation": "今天", "phonetic": "/təˈdeɪ/", "partOfSpeech": "n.", "etymology": "to-向 + day-日", "example": "Today is Monday.", "translation": "今天是星期一。"},
    {"word": "tomorrow", "wordTranslation": "明天", "phonetic": "/təˈmɒrəʊ/", "partOfSpeech": "n.", "etymology": "to-向 + morn-早晨", "example": "See you tomorrow.", "translation": "明天见。"},
    {"word": "yesterday", "wordTranslation": "昨天", "phonetic": "/ˈjestədeɪ/", "partOfSpeech": "n.", "etymology": "yester-昨晚 + day-日", "example": "Yesterday was fun.", "translation": "昨天很有趣。"},
    {"word": "week", "wordTranslation": "周", "phonetic": "/wiːk/", "partOfSpeech": "n.", "etymology": "来自古英语wice", "example": "This week is busy.", "translation": "这周很忙。"},
    {"word": "month", "wordTranslation": "月", "phonetic": "/mʌnθ/", "partOfSpeech": "n.", "etymology": "来自古英语monath", "example": "This month is hot.", "translation": "这个月很热。"},
    {"word": "year", "wordTranslation": "年", "phonetic": "/jɪər/", "partOfSpeech": "n.", "etymology": "来自古英语gear", "example": "Happy New Year!", "translation": "新年快乐！"},
    {"word": "hour", "wordTranslation": "小时", "phonetic": "/ˈaʊər/", "partOfSpeech": "n.", "etymology": "来自希腊语hora", "example": "Wait for one hour.", "translation": "等一个小时。"},
    {"word": "minute", "wordTranslation": "分钟", "phonetic": "/ˈmɪnɪt/", "partOfSpeech": "n.", "etymology": "来自拉丁语minuta", "example": "Just a minute.", "translation": "等一下。"},
    {"word": "second", "wordTranslation": "秒", "phonetic": "/ˈsekənd/", "partOfSpeech": "n.", "etymology": "sec-跟随 + -ond", "example": "Wait a second.", "translation": "等一下。"},

    # 天气
    {"word": "weather", "wordTranslation": "天气", "phonetic": "/ˈweðər/", "partOfSpeech": "n.", "etymology": "来自古英语weder", "example": "Nice weather today.", "translation": "今天天气好。"},
    {"word": "sunny", "wordTranslation": "阳光充足的", "phonetic": "/ˈsʌni/", "partOfSpeech": "adj.", "etymology": "sun-太阳 + -y", "example": "It's sunny today.", "translation": "今天阳光充足。"},
    {"word": "rainy", "wordTranslation": "下雨的", "phonetic": "/ˈreɪni/", "partOfSpeech": "adj.", "etymology": "rain-雨 + -y", "example": "It's rainy.", "translation": "下雨了。"},
    {"word": "cloudy", "wordTranslation": "多云的", "phonetic": "/ˈklaʊdi/", "partOfSpeech": "adj.", "etymology": "cloud-云 + -y", "example": "It's cloudy today.", "translation": "今天多云。"},
    {"word": "snowy", "wordTranslation": "下雪的", "phonetic": "/ˈsnəʊi/", "partOfSpeech": "adj.", "etymology": "snow-雪 + -y", "example": "It's snowy in winter.", "translation": "冬天下雪。"},
    {"word": "hot", "wordTranslation": "热的", "phonetic": "/hɒt/", "partOfSpeech": "adj.", "etymology": "来自古英语hat", "example": "It's very hot.", "translation": "很热。"},
    {"word": "cold", "wordTranslation": "冷的", "phonetic": "/kəʊld/", "partOfSpeech": "adj.", "etymology": "来自古英语ceald", "example": "It's cold outside.", "translation": "外面很冷。"},
    {"word": "warm", "wordTranslation": "暖和的", "phonetic": "/wɔːm/", "partOfSpeech": "adj.", "etymology": "来自古英语wearm", "example": "It's warm today.", "translation": "今天暖和。"},
    {"word": "cool", "wordTranslation": "凉爽的", "phonetic": "/kuːl/", "partOfSpeech": "adj.", "etymology": "来自古英语col", "example": "Cool weather is nice.", "translation": "凉爽的天气很舒服。"},
    {"word": "temperature", "wordTranslation": "温度", "phonetic": "/ˈtemprətʃər/", "partOfSpeech": "n.", "etymology": "temper-调节 + -ature", "example": "What's the temperature?", "translation": "温度是多少？"},

    # 健康
    {"word": "doctor", "wordTranslation": "医生", "phonetic": "/ˈdɒktər/", "partOfSpeech": "n.", "etymology": "doc-教 + -or", "example": "See a doctor.", "translation": "看医生。"},
    {"word": "hospital", "wordTranslation": "医院", "phonetic": "/ˈhɒspɪtəl/", "partOfSpeech": "n.", "etymology": "hospit-客人 + -al", "example": "Go to the hospital.", "translation": "去医院。"},
    {"word": "medicine", "wordTranslation": "药", "phonetic": "/ˈmedɪsɪn/", "partOfSpeech": "n.", "etymology": "med-治疗 + -icine", "example": "Take the medicine.", "translation": "吃药。"},
    {"word": "headache", "wordTranslation": "头痛", "phonetic": "/ˈhedeɪk/", "partOfSpeech": "n.", "etymology": "head-头 + ache-痛", "example": "I have a headache.", "translation": "我头痛。"},
    {"word": "fever", "wordTranslation": "发烧", "phonetic": "/ˈfiːvər/", "partOfSpeech": "n.", "etymology": "来自古英语fefer", "example": "She has a fever.", "translation": "她发烧了。"},
    {"word": "pain", "wordTranslation": "疼痛", "phonetic": "/peɪn/", "partOfSpeech": "n.", "etymology": "来自古法语poine", "example": "I feel pain.", "translation": "我感到疼痛。"},
    {"word": "healthy", "wordTranslation": "健康的", "phonetic": "/ˈhelθi/", "partOfSpeech": "adj.", "etymology": "health-健康 + -y", "example": "Stay healthy.", "translation": "保持健康。"},
    {"word": "sick", "wordTranslation": "生病的", "phonetic": "/sɪk/", "partOfSpeech": "adj.", "etymology": "来自古英语seoc", "example": "I feel sick.", "translation": "我感觉不舒服。"},
    {"word": "rest", "wordTranslation": "休息", "phonetic": "/rest/", "partOfSpeech": "v.", "etymology": "来自古英语ræst", "example": "You need to rest.", "translation": "你需要休息。"},
    {"word": "sleep", "wordTranslation": "睡觉", "phonetic": "/sliːp/", "partOfSpeech": "v.", "etymology": "来自古英语slaep", "example": "I sleep 8 hours.", "translation": "我睡8小时。"},

    # 工作和学习
    {"word": "work", "wordTranslation": "工作", "phonetic": "/wɜːk/", "partOfSpeech": "n.", "etymology": "来自古英语weorc", "example": "I go to work.", "translation": "我去上班。"},
    {"word": "job", "wordTranslation": "工作/职业", "phonetic": "/dʒɒb/", "partOfSpeech": "n.", "etymology": "可能来自jobbe（零工）", "example": "Find a new job.", "translation": "找新工作。"},
    {"word": "office", "wordTranslation": "办公室", "phonetic": "/ˈɒfɪs/", "partOfSpeech": "n.", "etymology": "ob-向 + fic-做 + -e", "example": "Work in the office.", "translation": "在办公室工作。"},
    {"word": "business", "wordTranslation": "商业", "phonetic": "/ˈbɪznəs/", "partOfSpeech": "n.", "etymology": "busy-忙碌 + -ness", "example": "It's business.", "translation": "这是生意。"},
    {"word": "meeting", "wordTranslation": "会议", "phonetic": "/ˈmiːtɪŋ/", "partOfSpeech": "n.", "etymology": "meet-见面 + -ing", "example": "Attend a meeting.", "translation": "参加会议。"},
    {"word": "school", "wordTranslation": "学校", "phonetic": "/skuːl/", "partOfSpeech": "n.", "etymology": "来自希腊语schole", "example": "Go to school.", "translation": "去学校。"},
    {"word": "student", "wordTranslation": "学生", "phonetic": "/ˈstjuːdənt/", "partOfSpeech": "n.", "etymology": "stud-学习 + -ent", "example": "I'm a student.", "translation": "我是学生。"},
    {"word": "teacher", "wordTranslation": "老师", "phonetic": "/ˈtiːtʃər/", "partOfSpeech": "n.", "etymology": "teach-教 + -er", "example": "The teacher is kind.", "translation": "老师很和善。"},
    {"word": "class", "wordTranslation": "课/班级", "phonetic": "/klɑːs/", "partOfSpeech": "n.", "etymology": "来自拉丁语classis", "example": "Go to class.", "translation": "去上课。"},
    {"word": "homework", "wordTranslation": "作业", "phonetic": "/ˈhəʊmwɜːk/", "partOfSpeech": "n.", "etymology": "home-家 + work-工作", "example": "Do your homework.", "translation": "做作业。"},

    # 通讯
    {"word": "phone", "wordTranslation": "电话", "phonetic": "/fəʊn/", "partOfSpeech": "n.", "etymology": "来自希腊语phone", "example": "Answer the phone.", "translation": "接电话。"},
    {"word": "message", "wordTranslation": "消息", "phonetic": "/ˈmesɪdʒ/", "partOfSpeech": "n.", "etymology": "miss-送 + -age", "example": "Send a message.", "translation": "发消息。"},
    {"word": "email", "wordTranslation": "电子邮件", "phonetic": "/ˈiːmeɪl/", "partOfSpeech": "n.", "etymology": "electronic mail", "example": "Check your email.", "translation": "查邮件。"},
    {"word": "internet", "wordTranslation": "互联网", "phonetic": "/ˈɪntənet/", "partOfSpeech": "n.", "etymology": "inter-之间 + net-网", "example": "Use the internet.", "translation": "用互联网。"},
    {"word": "computer", "wordTranslation": "电脑", "phonetic": "/kəmˈpjuːtər/", "partOfSpeech": "n.", "etymology": "com-一起 + put-想 + -er", "example": "Work on computer.", "translation": "用电脑工作。"},
    {"word": "website", "wordTranslation": "网站", "phonetic": "/ˈwebsaɪt/", "partOfSpeech": "n.", "etymology": "web-网 + site-地点", "example": "Visit this website.", "translation": "访问这个网站。"},
    {"word": "app", "wordTranslation": "应用程序", "phonetic": "/æp/", "partOfSpeech": "n.", "etymology": "application的缩写", "example": "Download this app.", "translation": "下载这个应用。"},
    {"word": "call", "wordTranslation": "打电话", "phonetic": "/kɔːl/", "partOfSpeech": "v.", "etymology": "来自古英语ceallian", "example": "Call me later.", "translation": "稍后打电话给我。"},
    {"word": "text", "wordTranslation": "发短信", "phonetic": "/tekst/", "partOfSpeech": "v.", "etymology": "来自拉丁语textus", "example": "Text me.", "translation": "发短信给我。"},
    {"word": "video", "wordTranslation": "视频", "phonetic": "/ˈvɪdiəʊ/", "partOfSpeech": "n.", "etymology": "来自拉丁语videre", "example": "Watch a video.", "translation": "看视频。"},

    # 社交
    {"word": "friend", "wordTranslation": "朋友", "phonetic": "/frend/", "partOfSpeech": "n.", "etymology": "来自古英语freond", "example": "My best friend.", "translation": "我最好的朋友。"},
    {"word": "neighbor", "wordTranslation": "邻居", "phonetic": "/ˈneɪbər/", "partOfSpeech": "n.", "etymology": "near-近 + bor-农民", "example": "Say hi to neighbor.", "translation": "和邻居打招呼。"},
    {"word": "party", "wordTranslation": "聚会", "phonetic": "/ˈpɑːti/", "partOfSpeech": "n.", "etymology": "来自古法语partie", "example": "Have a party.", "translation": "举办聚会。"},
    {"word": "birthday", "wordTranslation": "生日", "phonetic": "/ˈbɜːθdeɪ/", "partOfSpeech": "n.", "etymology": "birth-出生 + day-日", "example": "Happy birthday!", "translation": "生日快乐！"},
    {"word": "celebrate", "wordTranslation": "庆祝", "phonetic": "/ˈseləbreɪt/", "partOfSpeech": "v.", "etymology": "celer-快速 + -ate", "example": "Celebrate together.", "translation": "一起庆祝。"},
    {"word": "invitation", "wordTranslation": "邀请", "phonetic": "/ˌɪnvɪˈteɪʃən/", "partOfSpeech": "n.", "etymology": "in-内 + vit-生命 + -ation", "example": "Send an invitation.", "translation": "发送邀请。"},
    {"word": "guest", "wordTranslation": "客人", "phonetic": "/ɡest/", "partOfSpeech": "n.", "etymology": "来自古英语gæst", "example": "We have guests.", "translation": "我们有客人。"},
    {"word": "visit", "wordTranslation": "拜访", "phonetic": "/ˈvɪzɪt/", "partOfSpeech": "v.", "etymology": "vis-看 + -it", "example": "Visit friends.", "translation": "拜访朋友。"},
    {"word": "introduce", "wordTranslation": "介绍", "phonetic": "/ˌɪntrəˈdjuːs/", "partOfSpeech": "v.", "etymology": "intro-向内 + duc-引导 + -e", "example": "Let me introduce.", "translation": "让我介绍。"},
    {"word": "relationship", "wordTranslation": "关系", "phonetic": "/rɪˈleɪʃənʃɪp/", "partOfSpeech": "n.", "etymology": "re-回 + lat-带 + -ion + -ship", "example": "Good relationship.", "translation": "好关系。"},

    # 日常活动
    {"word": "morning", "wordTranslation": "早上", "phonetic": "/ˈmɔːnɪŋ/", "partOfSpeech": "n.", "etymology": "来自古英语morgen", "example": "Good morning.", "translation": "早上好。"},
    {"word": "afternoon", "wordTranslation": "下午", "phonetic": "/ˌɑːftəˈnuːn/", "partOfSpeech": "n.", "etymology": "after-之后 + noon-中午", "example": "Good afternoon.", "translation": "下午好。"},
    {"word": "evening", "wordTranslation": "晚上", "phonetic": "/ˈiːvnɪŋ/", "partOfSpeech": "n.", "etymology": "来自古英语æfnung", "example": "Good evening.", "translation": "晚上好。"},
    {"word": "night", "wordTranslation": "夜晚", "phonetic": "/naɪt/", "partOfSpeech": "n.", "etymology": "来自古英语neaht", "example": "Good night.", "translation": "晚安。"},
    {"word": "wake up", "wordTranslation": "起床", "phonetic": "/weɪk ʌp/", "partOfSpeech": "v.", "etymology": "wake-醒 + up-上", "example": "I wake up at 7.", "translation": "我7点起床。"},
    {"word": "brush teeth", "wordTranslation": "刷牙", "phonetic": "/brʌʃ tiːθ/", "partOfSpeech": "v.", "etymology": "brush-刷 + teeth-牙", "example": "Brush your teeth.", "translation": "刷牙。"},
    {"word": "shower", "wordTranslation": "淋浴", "phonetic": "/ˈʃaʊər/", "partOfSpeech": "n.", "etymology": "来自古法语escur", "example": "Take a shower.", "translation": "淋浴。"},
    {"word": "cook", "wordTranslation": "做饭", "phonetic": "/kʊk/", "partOfSpeech": "v.", "etymology": "来自古英语cooc", "example": "I cook dinner.", "translation": "我做晚饭。"},
    {"word": "clean", "wordTranslation": "打扫", "phonetic": "/kliːn/", "partOfSpeech": "v.", "etymology": "来自古英语clæne", "example": "Clean the house.", "translation": "打扫房子。"},
    {"word": "wash", "wordTranslation": "洗", "phonetic": "/wɒʃ/", "partOfSpeech": "v.", "etymology": "来自古英语wæscan", "example": "Wash your hands.", "translation": "洗手。"},

    # 情感
    {"word": "happy", "wordTranslation": "快乐的", "phonetic": "/ˈhæpi/", "partOfSpeech": "adj.", "etymology": "hap-运气 + -y", "example": "I am happy.", "translation": "我很快乐。"},
    {"word": "sad", "wordTranslation": "伤心的", "phonetic": "/sæd/", "partOfSpeech": "adj.", "etymology": "来自古英语sæd", "example": "Don't be sad.", "translation": "别伤心。"},
    {"word": "angry", "wordTranslation": "生气的", "phonetic": "/ˈæŋɡri/", "partOfSpeech": "adj.", "etymology": "angr-愤怒 + -y", "example": "Don't be angry.", "translation": "别生气。"},
    {"word": "tired", "wordTranslation": "累的", "phonetic": "/ˈtaɪərd/", "partOfSpeech": "adj.", "etymology": "tire-疲劳 + -ed", "example": "I'm tired.", "translation": "我累了。"},
    {"word": "excited", "wordTranslation": "兴奋的", "phonetic": "/ɪkˈsaɪtɪd/", "partOfSpeech": "adj.", "etymology": "ex-出 + cit-驱动 + -ed", "example": "I'm excited.", "translation": "我很兴奋。"},
    {"word": "worried", "wordTranslation": "担心的", "phonetic": "/ˈwʌrɪd/", "partOfSpeech": "adj.", "etymology": "worry-担心 + -ed", "example": "Don't be worried.", "translation": "别担心。"},
    {"word": "love", "wordTranslation": "爱", "phonetic": "/lʌv/", "partOfSpeech": "v.", "etymology": "来自古英语lufu", "example": "I love you.", "translation": "我爱你。"},
    {"word": "miss", "wordTranslation": "想念/错过", "phonetic": "/mɪs/", "partOfSpeech": "v.", "etymology": "来自古英语missan", "example": "I miss you.", "translation": "我想你。"},
    {"word": "hope", "wordTranslation": "希望", "phonetic": "/həʊp/", "partOfSpeech": "v.", "etymology": "来自古英语hopa", "example": "I hope so.", "translation": "我希望如此。"},
    {"word": "thank", "wordTranslation": "感谢", "phonetic": "/θæŋk/", "partOfSpeech": "v.", "etymology": "来自古英语thancian", "example": "Thank you.", "translation": "谢谢你。"},

    # 其他常用
    {"word": "help", "wordTranslation": "帮助", "phonetic": "/help/", "partOfSpeech": "v.", "etymology": "来自古英语helpan", "example": "Can you help me?", "translation": "你能帮我吗？"},
    {"word": "need", "wordTranslation": "需要", "phonetic": "/niːd/", "partOfSpeech": "v.", "etymology": "来自古英语ned", "example": "I need this.", "translation": "我需要这个。"},
    {"word": "want", "wordTranslation": "想要", "phonetic": "/wɒnt/", "partOfSpeech": "v.", "etymology": "来自古英语won", "example": "I want to go.", "translation": "我想去。"},
    {"word": "like", "wordTranslation": "喜欢", "phonetic": "/laɪk/", "partOfSpeech": "v.", "etymology": "来自古英语gelic", "example": "I like music.", "translation": "我喜欢音乐。"},
    {"word": "hate", "wordTranslation": "讨厌", "phonetic": "/heɪt/", "partOfSpeech": "v.", "etymology": "来自古英语hatian", "example": "I hate waiting.", "translation": "我讨厌等待。"},
    {"word": "try", "wordTranslation": "尝试", "phonetic": "/traɪ/", "partOfSpeech": "v.", "etymology": "来自古英语treowan", "example": "Try again.", "translation": "再试一次。"},
    {"word": "use", "wordTranslation": "使用", "phonetic": "/juːz/", "partOfSpeech": "v.", "etymology": "来自拉丁语uti", "example": "Use it.", "translation": "使用它。"},
    {"word": "find", "wordTranslation": "找到", "phonetic": "/faɪnd/", "partOfSpeech": "v.", "etymology": "来自古英语findan", "example": "Find a job.", "translation": "找工作。"},
    {"word": "think", "wordTranslation": "想/认为", "phonetic": "/θɪŋk/", "partOfSpeech": "v.", "etymology": "来自古英语thenc", "example": "I think so.", "translation": "我也这么认为。"},
    {"word": "know", "wordTranslation": "知道", "phonetic": "/nəʊ/", "partOfSpeech": "v.", "etymology": "来自古英语cnawan", "example": "I don't know.", "translation": "我不知道。"},
]

for w in words:
    note = genanki.Note(
        model=my_model,
        fields=[w['word'], w['wordTranslation'], w['phonetic'], w['partOfSpeech'], w['etymology'], w['example'], w['translation']]
    )
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file('/workspace/daily_life_vocabulary.apkg')
print(f'daily_life_vocabulary.apkg 已生成！共 {len(words)} 个单词')
