import genanki

my_model = genanki.Model(
    1234567890,
    'Fitness Dictionary Model',
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

deck = genanki.Deck(9876543211, 'Fitness Vocabulary')

words = [
    # 基础健身词汇
    {"word": "fitness", "wordTranslation": "健身/健康", "phonetic": "/ˈfɪtnəs/", "partOfSpeech": "n.", "etymology": "fit-适合 + -ness状态", "example": "Fitness is important for health.", "translation": "健身对健康很重要。"},
    {"word": "workout", "wordTranslation": "锻炼/训练", "phonetic": "/ˈwɜːkaʊt/", "partOfSpeech": "n.", "etymology": "work-工作 + out-出", "example": "I do a workout every morning.", "translation": "我每天早上锻炼。"},
    {"word": "exercise", "wordTranslation": "运动/练习", "phonetic": "/ˈeksəsaɪz/", "partOfSpeech": "n.", "etymology": "ex-出 + erc-推动 + -ise", "example": "Regular exercise is beneficial.", "translation": "经常运动是有益的。"},
    {"word": "gym", "wordTranslation": "健身房", "phonetic": "/dʒɪm/", "partOfSpeech": "n.", "etymology": "gymnasium-体育馆的缩写", "example": "I go to the gym three times a week.", "translation": "我一周去三次健身房。"},
    {"word": "training", "wordTranslation": "训练", "phonetic": "/ˈtreɪnɪŋ/", "partOfSpeech": "n.", "etymology": "train-火车/培训 + -ing", "example": "His training routine is intense.", "translation": "他的训练安排很紧张。"},
    {"word": "muscle", "wordTranslation": "肌肉", "phonetic": "/ˈmʌsəl/", "partOfSpeech": "n.", "etymology": "来自拉丁语musculus（小老鼠）", "example": "Building muscle requires protein.", "translation": "增肌需要蛋白质。"},
    {"word": "strength", "wordTranslation": "力量", "phonetic": "/streŋθ/", "partOfSpeech": "n.", "etymology": "strong-强壮 + -th", "example": "Strength training builds muscle.", "translation": "力量训练增肌。"},
    {"word": "endurance", "wordTranslation": "耐力", "phonetic": "/ɪnˈdjʊərəns/", "partOfSpeech": "n.", "etymology": "en-使 + dur-持续 + -ance", "example": "Cardio improves endurance.", "translation": "有氧运动提高耐力。"},
    {"word": "flexibility", "wordTranslation": "柔韧性", "phonetic": "/ˌfleksəˈbɪləti/", "partOfSpeech": "n.", "etymology": "flex-弯曲 + -ibility", "example": "Stretching improves flexibility.", "translation": "拉伸提高柔韧性。"},
    {"word": "balance", "wordTranslation": "平衡", "phonetic": "/ˈbæləns/", "partOfSpeech": "n.", "etymology": "来自拉丁语bilanx（双秤盘）", "example": "Balance is key to stability.", "translation": "平衡是稳定的关键。"},

    # 器械和设备
    {"word": "dumbbell", "wordTranslation": "哑铃", "phonetic": "/ˈdʌmbel/", "partOfSpeech": "n.", "etymology": "dumb-哑的 + bell-铃", "example": "Lift the dumbbell carefully.", "translation": "小心举起哑铃。"},
    {"word": "barbell", "wordTranslation": "杠铃", "phonetic": "/ˈbɑːbel/", "partOfSpeech": "n.", "etymology": "bar-棒 + bell-铃", "example": "The barbell weighs 20 kilograms.", "translation": "杠铃重20公斤。"},
    {"word": "treadmill", "wordTranslation": "跑步机", "phonetic": "/ˈtredmɪl/", "partOfSpeech": "n.", "etymology": "tread-踩 + mill-磨坊", "example": "Run on the treadmill for 30 minutes.", "translation": "在跑步机上跑30分钟。"},
    {"word": "bench", "wordTranslation": "长凳/卧推凳", "phonetic": "/bentʃ/", "partOfSpeech": "n.", "etymology": "来自古英语benc", "example": "Press on the flat bench.", "translation": "在平凳上卧推。"},
    {"word": "kettlebell", "wordTranslation": "壶铃", "phonetic": "/ˈketəlbel/", "partOfSpeech": "n.", "etymology": "kettle-壶 + bell-铃", "example": "Swing the kettlebell.", "translation": "摆动壶铃。"},
    {"word": "resistance band", "wordTranslation": "弹力带", "phonetic": "/rɪˈzɪstəns bænd/", "partOfSpeech": "n.", "etymology": "resistance-阻力 + band-带", "example": "Use a resistance band for练习.", "translation": "用弹力带练习。"},
    {"word": "pull-up bar", "wordTranslation": "引体向上杆", "phonetic": "/pʊl-ʌp bɑːr/", "partOfSpeech": "n.", "etymology": "pull-拉 + up-上 + bar-杆", "example": "Do pull-ups on the bar.", "translation": "在单杠上做引体向上。"},
    {"word": "squat rack", "wordTranslation": "深蹲架", "phonetic": "/skwɒt ræk/", "partOfSpeech": "n.", "etymology": "squat-蹲 + rack-架子", "example": "Set up the squat rack.", "translation": "设置深蹲架。"},
    {"word": "cable machine", "wordTranslation": "绳索训练器", "phonetic": "/ˈkeɪbəl məˈʃiːn/", "partOfSpeech": "n.", "etymology": "cable-缆绳 + machine-机器", "example": "Use the cable machine for rows.", "translation": "用绳索训练器做划船。"},
    {"word": "rowing machine", "wordTranslation": "划船机", "phonetic": "/ˈrəʊɪŋ məˈʃiːn/", "partOfSpeech": "n.", "etymology": "row-划船 + machine-机器", "example": "I like the rowing machine.", "translation": "我喜欢划船机。"},

    # 动作词汇
    {"word": "squat", "wordTranslation": "深蹲", "phonetic": "/skwɒt/", "partOfSpeech": "v.", "etymology": "来自低地德语schquat", "example": "Do a deep squat.", "translation": "做一个深蹲。"},
    {"word": "lunges", "wordTranslation": "弓步", "phonetic": "/lʌndʒɪz/", "partOfSpeech": "n.", "etymology": "来自古法语longer（向前冲）", "example": "Perform walking lunges.", "translation": "做行进弓步。"},
    {"word": "push-up", "wordTranslation": "俯卧撑", "phonetic": "/pʊʃ-ʌp/", "partOfSpeech": "n.", "etymology": "push-推 + up-上", "example": "Do 20 push-ups.", "translation": "做20个俯卧撑。"},
    {"word": "pull-up", "wordTranslation": "引体向上", "phonetic": "/pʊl-ʌp/", "partOfSpeech": "n.", "etymology": "pull-拉 + up-上", "example": "He can do ten pull-ups.", "translation": "他能做10个引体向上。"},
    {"word": "deadlift", "wordTranslation": "硬拉", "phonetic": "/ˈdedlɪft/", "partOfSpeech": "n.", "etymology": "dead-死的 + lift-拉", "example": "The deadlift works your back.", "translation": "硬拉锻炼背部。"},
    {"word": "bench press", "wordTranslation": "卧推", "phonetic": "/bentʃ pres/", "partOfSpeech": "n.", "etymology": "bench-凳 + press-推", "example": "His bench press max is 100kg.", "translation": "他的卧推最大重量是100公斤。"},
    {"word": "curl", "wordTranslation": "弯举", "phonetic": "/kɜːl/", "partOfSpeech": "n.", "etymology": "来自古英语curl（卷曲）", "example": "Bicep curls build arm strength.", "translation": "二头肌弯举增强臂力。"},
    {"word": "extension", "wordTranslation": "伸展", "phonetic": "/ɪkˈstenʃən/", "partOfSpeech": "n.", "etymology": "ex-出 + tens-伸 + -ion", "example": "Leg extensions target quads.", "translation": "腿伸展针对股四头肌。"},
    {"word": "raise", "wordTranslation": "侧平举", "phonetic": "/reɪz/", "partOfSpeech": "n.", "etymology": "raise-举起", "example": "Lateral raises for shoulders.", "translation": "侧平举锻炼肩部。"},
    {"word": "press", "wordTranslation": "推举", "phonetic": "/pres/", "partOfSpeech": "n.", "etymology": "来自拉丁语pressare（压）", "example": "Overhead press for shoulders.", "translation": "肩部推举。"},

    # 有氧运动
    {"word": "cardio", "wordTranslation": "有氧运动", "phonetic": "/ˈkɑːdiəʊ/", "partOfSpeech": "n.", "etymology": "cardio-心脏", "example": "Cardio burns calories.", "translation": "有氧运动燃烧卡路里。"},
    {"word": "running", "wordTranslation": "跑步", "phonetic": "/ˈrʌnɪŋ/", "partOfSpeech": "n.", "etymology": "run-跑 + -ing", "example": "Running improves cardio health.", "translation": "跑步改善心血管健康。"},
    {"word": "jogging", "wordTranslation": "慢跑", "phonetic": "/ˈdʒɒɡɪŋ/", "partOfSpeech": "n.", "etymology": "jog-轻推 + -ing", "example": "Go jogging in the park.", "translation": "去公园慢跑。"},
    {"word": "cycling", "wordTranslation": "骑行", "phonetic": "/ˈsaɪklɪŋ/", "partOfSpeech": "n.", "etymology": "cycl-圆 + -ing", "example": "Cycling is great cardio.", "translation": "骑行是很棒的有氧运动。"},
    {"word": "swimming", "wordTranslation": "游泳", "phonetic": "/ˈswɪmɪŋ/", "partOfSpeech": "n.", "etymology": "swim-游泳 + -ing", "example": "Swimming works your whole body.", "translation": "游泳锻炼全身。"},
    {"word": "jump rope", "wordTranslation": "跳绳", "phonetic": "/dʒʌmp rəʊp/", "partOfSpeech": "n.", "etymology": "jump-跳 + rope-绳", "example": "Jump rope for 10 minutes.", "translation": "跳绳10分钟。"},
    {"word": "HIIT", "wordTranslation": "高强度间歇训练", "phonetic": "/hɪt/", "partOfSpeech": "abbr.", "etymology": "High Intensity Interval Training", "example": "HIIT is very effective.", "translation": "高强度间歇训练非常有效。"},
    {"word": "stair climber", "wordTranslation": "爬楼梯机", "phonetic": "/steər ˈklaɪmər/", "partOfSpeech": "n.", "etymology": "stair-楼梯 + climber-攀爬者", "example": "Use the stair climber.", "translation": "用爬楼梯机。"},
    {"word": "elliptical", "wordTranslation": "椭圆机", "phonetic": "/ɪˈlɪptɪkəl/", "partOfSpeech": "n.", "etymology": "ellipse-椭圆 + -al", "example": "The elliptical is low impact.", "translation": "椭圆机对关节冲击小。"},
    {"word": "aerobics", "wordTranslation": "有氧操", "phonetic": "/eəˈrəʊbɪks/", "partOfSpeech": "n.", "etymology": "aero-空气 + -bics", "example": "She teaches aerobics class.", "translation": "她教有氧操课。"},

    # 肌肉部位
    {"word": "bicep", "wordTranslation": "二头肌", "phonetic": "/ˈbaɪsep/", "partOfSpeech": "n.", "etymology": "bi-二 + cep-头", "example": "Curl to build your bicep.", "translation": "弯举锻炼二头肌。"},
    {"word": "tricep", "wordTranslation": "三头肌", "phonetic": "/ˈtraɪsep/", "partOfSpeech": "n.", "etymology": "tri-三 + cep-头", "example": "Tricep dips target the tricep.", "translation": "三头肌下压针对三头肌。"},
    {"word": "quadriceps", "wordTranslation": "股四头肌", "phonetic": "/ˈkwɒdrɪseps/", "partOfSpeech": "n.", "etymology": "quadri-四 + ceps-头", "example": "Squats work the quadriceps.", "translation": "深蹲锻炼股四头肌。"},
    {"word": "hamstring", "wordTranslation": "腘绳肌", "phonetic": "/ˈhæmstrɪŋ/", "partOfSpeech": "n.", "etymology": "ham-腿窝 + string-绳", "example": "Stretch your hamstrings.", "translation": "拉伸腘绳肌。"},
    {"word": "deltoid", "wordTranslation": "三角肌", "phonetic": "/ˈdeltɔɪd/", "partOfSpeech": "n.", "etymology": "delta-希腊字母Δ + -oid", "example": "Shoulders are deltoids.", "translation": "肩部是三角肌。"},
    {"word": "pectoral", "wordTranslation": "胸肌", "phonetic": "/pekˈtɒrəl/", "partOfSpeech": "n.", "etymology": "pect-胸 + -oral", "example": "Bench press builds pectorals.", "translation": "卧推锻炼胸肌。"},
    {"word": "abdominal", "wordTranslation": "腹肌", "phonetic": "/æbˈdɒmɪnəl/", "partOfSpeech": "n.", "etymology": "abdom-腹部 + -inal", "example": "Planks strengthen abdominals.", "translation": "平板支撑加强腹肌。"},
    {"word": "gluteus", "wordTranslation": "臀肌", "phonetic": "/ˈɡluːtiəs/", "partOfSpeech": "n.", "etymology": "来自希腊语gloutos（臀部）", "example": "Hip thrusts activate gluteus.", "translation": "臀推激活臀肌。"},
    {"word": "calf", "wordTranslation": "小腿肌", "phonetic": "/kɑːf/", "partOfSpeech": "n.", "etymology": "来自古英语cealf", "example": "Calf raises target calves.", "translation": "提踵针对小腿肌。"},
    {"word": "forearm", "wordTranslation": "前臂", "phonetic": "/ˈfɔːrɑːm/", "partOfSpeech": "n.", "etymology": "fore-前 + arm-臂", "example": "Wrist curls work forearms.", "translation": "腕弯举锻炼前臂。"},

    # 健身计划
    {"word": "routine", "wordTranslation": "常规/日程", "phonetic": "/ruːˈtiːn/", "partOfSpeech": "n.", "etymology": "route-路线 + -ine", "example": "Establish a workout routine.", "translation": "建立锻炼日程。"},
    {"word": "repetition", "wordTranslation": "重复次数", "phonetic": "/ˌrepɪˈtɪʃən/", "partOfSpeech": "n.", "etymology": "re-再 + pet-寻求 + -ition", "example": "Do 12 repetitions.", "translation": "做12次重复。"},
    {"word": "rep", "wordTranslation": "一次", "phonetic": "/rep/", "partOfSpeech": "n.", "etymology": "repetition的缩写", "example": "Three sets of 10 reps.", "translation": "三组每组10次。"},
    {"word": "set", "wordTranslation": "组", "phonetic": "/set/", "partOfSpeech": "n.", "etymology": "来自古英语set", "example": "Complete three sets.", "translation": "完成三组。"},
    {"word": "rest", "wordTranslation": "休息", "phonetic": "/rest/", "partOfSpeech": "n.", "etymology": "来自古英语ræst", "example": "Rest for 60 seconds.", "translation": "休息60秒。"},
    {"word": "warm-up", "wordTranslation": "热身", "phonetic": "/wɔːm-ʌp/", "partOfSpeech": "n.", "etymology": "warm-暖 + up-上", "example": "Always warm up before exercise.", "translation": "运动前一定要热身。"},
    {"word": "cool-down", "wordTranslation": "放松", "phonetic": "/kuːl-daʊn/", "partOfSpeech": "n.", "etymology": "cool-冷却 + down-下", "example": "Cool down after workout.", "translation": "锻炼后要放松。"},
    {"word": "progressive overload", "wordTranslation": "渐进超负荷", "phonetic": "/prəˈɡresɪv ˌəʊvəˈləʊd/", "partOfSpeech": "n.", "etymology": "progressive-渐进的 + overload-超负荷", "example": "Use progressive overload.", "translation": "使用渐进超负荷原则。"},
    {"word": "progression", "wordTranslation": "进阶", "phonetic": "/prəˈɡreʃən/", "partOfSpeech": "n.", "etymology": "pro-向前 + gress-走 + -ion", "example": "Track your progression.", "translation": "追踪你的进阶。"},
    {"word": "periodization", "wordTranslation": "周期化训练", "phonetic": "/ˌpɪəriədaɪˈzeɪʃən/", "partOfSpeech": "n.", "etymology": "period-周期 + -ization", "example": "Use periodization in training.", "translation": "训练中使用周期化。"},

    # 营养和饮食
    {"word": "protein", "wordTranslation": "蛋白质", "phonetic": "/ˈprəʊtiːn/", "partOfSpeech": "n.", "etymology": "proto-原始 + -ine", "example": "Muscles need protein.", "translation": "肌肉需要蛋白质。"},
    {"word": "carbohydrate", "wordTranslation": "碳水化合物", "phonetic": "/ˌkɑːbəˈhaɪdreɪt/", "partOfSpeech": "n.", "etymology": "carbo-碳 + hydr-水 + -ate", "example": "Carbs provide energy.", "translation": "碳水提供能量。"},
    {"word": "fat", "wordTranslation": "脂肪", "phonetic": "/fæt/", "partOfSpeech": "n.", "etymology": "来自古英语fætt", "example": "Healthy fats are essential.", "translation": "健康脂肪是必需的。"},
    {"word": "calorie", "wordTranslation": "卡路里", "phonetic": "/ˈkæləri/", "partOfSpeech": "n.", "etymology": "calor-热 + -ie", "example": "Count your calories.", "translation": "计算你的卡路里。"},
    {"word": "macronutrient", "wordTranslation": "常量营养素", "phonetic": "/ˌmækrəʊˈnjuːtriənt/", "partOfSpeech": "n.", "etymology": "macro-大 + nutrient-营养素", "example": "Track your macronutrients.", "translation": "追踪你的常量营养素。"},
    {"word": "micronutrient", "wordTranslation": "微量营养素", "phonetic": "/ˌmaɪkrəʊˈnjuːtriənt/", "partOfSpeech": "n.", "etymology": "micro-小 + nutrient-营养素", "example": "Vitamins are micronutrients.", "translation": "维生素是微量营养素。"},
    {"word": "supplement", "wordTranslation": "补剂", "phonetic": "/ˈsʌplɪmənt/", "partOfSpeech": "n.", "etymology": "sup-下 + ple-填满 + -ment", "example": "Take protein supplement.", "translation": "服用蛋白质补剂。"},
    {"word": "creatine", "wordTranslation": "肌酸", "phonetic": "/ˈkriːətɪn/", "partOfSpeech": "n.", "etymology": "creat-创造 + -ine", "example": "Creatine boosts strength.", "translation": "肌酸增强力量。"},
    {"word": "pre-workout", "wordTranslation": "训练前补剂", "phonetic": "/priː-ˈwɜːkaʊt/", "partOfSpeech": "n.", "etymology": "pre-前 + workout-锻炼", "example": "Take pre-workout before training.", "translation": "训练前服用补剂。"},
    {"word": "whey", "wordTranslation": "乳清", "phonetic": "/weɪ/", "partOfSpeech": "n.", "etymology": "来自古英语hwæg", "example": "Whey protein after workout.", "translation": "锻炼后喝乳清蛋白。"},

    # 健康和恢复
    {"word": "recovery", "wordTranslation": "恢复", "phonetic": "/rɪˈkʌvəri/", "partOfSpeech": "n.", "etymology": "re-回 + cover-覆盖 + -y", "example": "Rest is important for recovery.", "translation": "休息对恢复很重要。"},
    {"word": "hydration", "wordTranslation": "补水", "phonetic": "/haɪˈdreɪʃən/", "partOfSpeech": "n.", "etymology": "hydr-水 + -ation", "example": "Stay on top of hydration.", "translation": "保持充足水分。"},
    {"word": "stretching", "wordTranslation": "拉伸", "phonetic": "/ˈstretʃɪŋ/", "partOfSpeech": "n.", "etymology": "stretch-拉伸 + -ing", "example": "Stretching prevents injury.", "translation": "拉伸防止受伤。"},
    {"word": "mobility", "wordTranslation": "灵活性", "phonetic": "/məʊˈbɪləti/", "partOfSpeech": "n.", "etymology": "mob-动 + -ility", "example": "Improve your mobility.", "translation": "提高你的灵活性。"},
    {"word": "injury", "wordTranslation": "受伤", "phonetic": "/ˈɪndʒəri/", "partOfSpeech": "n.", "etymology": "in-不 + jur-法 + -y", "example": "Avoid injury at the gym.", "translation": "在健身房避免受伤。"},
    {"word": "strain", "wordTranslation": "拉伤", "phonetic": "/streɪn/", "partOfSpeech": "n.", "etymology": "来自古法语estraindre", "example": "Muscle strain needs rest.", "translation": "肌肉拉伤需要休息。"},
    {"word": "sprain", "wordTranslation": "扭伤", "phonetic": "/spreɪn/", "partOfSpeech": "n.", "etymology": "来自古法语espreindre", "example": "Ankle sprain is common.", "translation": "踝关节扭伤很常见。"},
    {"word": "inflammation", "wordTranslation": "炎症", "phonetic": "/ˌɪnfləˈmeɪʃən/", "partOfSpeech": "n.", "etymology": "in-内 + flamm-火焰 + -ation", "example": "Reduce inflammation.", "translation": "减少炎症。"},
    {"word": "massage", "wordTranslation": "按摩", "phonetic": "/ˈmæsɑːʒ/", "partOfSpeech": "n.", "etymology": "来自法语masser（揉捏）", "example": "Get a massage for recovery.", "translation": "按摩帮助恢复。"},
    {"word": "foam roller", "wordTranslation": "泡沫轴", "phonetic": "/fəʊm ˈrəʊlər/", "partOfSpeech": "n.", "etymology": "foam-泡沫 + roller-滚筒", "example": "Use a foam roller.", "translation": "使用泡沫轴。"},

    # 健身术语
    {"word": "bodybuilding", "wordTranslation": "健美", "phonetic": "/ˈbɒdibɪldɪŋ/", "partOfSpeech": "n.", "etymology": "body-身体 + building-建造", "example": "Bodybuilding requires discipline.", "translation": "健美需要自律。"},
    {"word": "physique", "wordTranslation": "体型", "phonetic": "/fɪˈziːk/", "partOfSpeech": "n.", "etymology": "来自希腊语physikos（自然的）", "example": "He has a great physique.", "translation": "他有很棒的体型。"},
    {"word": "bulking", "wordTranslation": "增肌期", "phonetic": "/ˈbʌlkɪŋ/", "partOfSpeech": "n.", "etymology": "bulk-大量 + -ing", "example": "Eat more during bulking.", "translation": "增肌期多吃。"},
    {"word": "cutting", "wordTranslation": "减脂期", "phonetic": "/ˈkʌtɪŋ/", "partOfSpeech": "n.", "etymology": "cut-切 + -ing", "example": "Reduce carbs during cutting.", "translation": "减脂期减少碳水。"},
    {"word": "shredding", "wordTranslation": "刷脂", "phonetic": "/ˈʃredɪŋ/", "partOfSpeech": "n.", "etymology": "shred-撕碎 + -ing", "example": "Shredding for summer.", "translation": "为夏天刷脂。"},
    {"word": "maintenance", "wordTranslation": "维持期", "phonetic": "/ˈmeɪntənəns/", "partOfSpeech": "n.", "etymology": "main-手 + ten-握 + -ance", "example": "Calorie maintenance level.", "translation": "卡路里维持水平。"},
    {"word": "deficit", "wordTranslation": "赤字/热量缺口", "phonetic": "/ˈdefɪsɪt/", "partOfSpeech": "n.", "etymology": "de-下 + fic-做 + -it", "example": "Create a calorie deficit.", "translation": "创造热量缺口。"},
    {"word": "surplus", "wordTranslation": "剩余/热量盈余", "phonetic": "/ˈsɜːpləs/", "partOfSpeech": "n.", "etymology": "sur-超过 + plus-加", "example": "Eat at a surplus to bulk.", "translation": "增肌要吃热量盈余。"},
    {"word": "body fat", "wordTranslation": "体脂", "phonetic": "/ˈbɒdi fæt/", "partOfSpeech": "n.", "etymology": "body-身体 + fat-脂肪", "example": "His body fat is 15%.", "translation": "他的体脂是15%。"},
    {"word": "lean", "wordTranslation": "瘦的/精瘦", "phonetic": "/liːn/", "partOfSpeech": "adj.", "etymology": "来自古英语hlæne", "example": "Stay lean year-round.", "translation": "全年保持精瘦。"},

    # 教练和课程
    {"word": "trainer", "wordTranslation": "教练", "phonetic": "/ˈtreɪnər/", "partOfSpeech": "n.", "etymology": "train-训练 + -er人", "example": "Hire a personal trainer.", "translation": "聘请私人教练。"},
    {"word": "instructor", "wordTranslation": "指导员", "phonetic": "/ɪnˈstrʌktər/", "partOfSpeech": "n.", "etymology": "in-内 + struct-建造 + -or", "example": "Follow the instructor.", "translation": "跟着指导员做。"},
    {"word": "spotter", "wordTranslation": "保护员", "phonetic": "/ˈspɒtər/", "partOfSpeech": "n.", "etymology": "spot-看 + -er人", "example": "Use a spotter for heavy lifts.", "translation": "大重量训练要用保护员。"},
    {"word": "group class", "wordTranslation": "团课", "phonetic": "/ɡruːp klɑːs/", "partOfSpeech": "n.", "etymology": "group-组 + class-课", "example": "Join a group class.", "translation": "参加团课。"},
    {"word": "yoga", "wordTranslation": "瑜伽", "phonetic": "/ˈjəʊɡə/", "partOfSpeech": "n.", "etymology": "来自梵语yuj（连接）", "example": "Practice yoga for flexibility.", "translation": "练瑜伽提高柔韧性。"},
    {"word": "pilates", "wordTranslation": "普拉提", "phonetic": "/pɪˈlɑːtiːz/", "partOfSpeech": "n.", "etymology": "以Joseph Pilates命名", "example": "Pilates strengthens core.", "translation": "普拉提加强核心。"},
    {"word": "crossfit", "wordTranslation": "CrossFit训练", "phonetic": "/krɒsfɪt/", "partOfSpeech": "n.", "etymology": "cross-交叉 + fit-健身", "example": "CrossFit is intense.", "translation": "CrossFit很激烈。"},
    {"word": "spin class", "wordTranslation": "动感单车课", "phonetic": "/spɪn klɑːs/", "partOfSpeech": "n.", "etymology": "spin-旋转 + class-课", "example": "Take a spin class.", "translation": "上动感单车课。"},
    {"word": "zumba", "wordTranslation": "尊巴舞", "phonetic": "/ˈzʊmbə/", "partOfSpeech": "n.", "etymology": "来自西班牙语zumba（派对）", "example": "Zumba is fun cardio.", "translation": "尊巴是有趣的有氧运动。"},
    {"word": "circuit", "wordTranslation": "循环训练", "phonetic": "/ˈsɜːkɪt/", "partOfSpeech": "n.", "etymology": "circ-圆 + -it", "example": "Do a circuit workout.", "translation": "做循环训练。"},

    # 更多动作
    {"word": "plank", "wordTranslation": "平板支撑", "phonetic": "/plæŋk/", "partOfSpeech": "n.", "etymology": "来自古英语planka（板）", "example": "Hold the plank for 60 seconds.", "translation": "保持平板支撑60秒。"},
    {"word": "crunch", "wordTranslation": "卷腹", "phonetic": "/krʌntʃ/", "partOfSpeech": "n.", "etymology": "crunch-脆响", "example": "Do abdominal crunches.", "translation": "做卷腹。"},
    {"word": "mountain climber", "wordTranslation": "登山者", "phonetic": "/ˈmaʊntɪn ˈmaɪlər/", "partOfSpeech": "n.", "etymology": "mountain-山 + climber-攀爬者", "example": "Mountain climbers cardio.", "translation": "登山者是有氧训练。"},
    {"word": "burpee", "wordTranslation": "波比跳", "phonetic": "/ˈbɜːpi/", "partOfSpeech": "n.", "etymology": "以Royal Burpee命名", "example": "Burpees are intense.", "translation": "波比跳很激烈。"},
    {"word": "jumping jack", "wordTranslation": "开合跳", "phonetic": "/ˈdʒʌmpɪŋ dʒæk/", "partOfSpeech": "n.", "etymology": "jumping-跳 + jack-杰克", "example": "Do jumping jacks to warm up.", "translation": "做开合跳热身。"},
    {"word": "sit-up", "wordTranslation": "仰卧起坐", "phonetic": "/ˈsɪt-ʌp/", "partOfSpeech": "n.", "etymology": "sit-坐 + up-上", "example": "Do 50 sit-ups.", "translation": "做50个仰卧起坐。"},
    {"word": "leg raise", "wordTranslation": "举腿", "phonetic": "/leɡ reɪz/", "partOfSpeech": "n.", "etymology": "leg-腿 + raise-举起", "example": "Leg raises for abs.", "translation": "举腿锻炼腹肌。"},
    {"word": "hip thrust", "wordTranslation": "臀推", "phonetic": "/hɪp θrʌst/", "partOfSpeech": "n.", "etymology": "hip-臀 + thrust-推", "example": "Hip thrusts for glutes.", "translation": "臀推锻炼臀肌。"},
    {"word": "shoulder press", "wordTranslation": "肩部推举", "phonetic": "/ˈʃəʊldər pres/", "partOfSpeech": "n.", "etymology": "shoulder-肩 + press-推", "example": "Seated shoulder press.", "translation": "坐姿肩部推举。"},
    {"word": "lat pulldown", "wordTranslation": "高位下拉", "phonetic": "/læt pʊlˈdaʊn/", "partOfSpeech": "n.", "etymology": "lat-背阔肌 + pulldown-下拉", "example": "Wide-grip lat pulldown.", "translation": "宽握高位下拉。"},

    # 健身成果
    {"word": "gains", "wordTranslation": "进步/增肌", "phonetic": "/ɡeɪnz/", "partOfSpeech": "n.", "etymology": "gain-获得 + -s复数", "example": "Make some serious gains.", "translation": "取得真正的进步。"},
    {"word": "progress", "wordTranslation": "进步", "phonetic": "/ˈprəʊɡres/", "partOfSpeech": "n.", "etymology": "pro-向前 + gress-走", "example": "Track your progress.", "translation": "追踪你的进步。"},
    {"word": "target", "wordTranslation": "针对", "phonetic": "/ˈtɑːɡɪt/", "partOfSpeech": "v.", "etymology": "来自古法语targette（小盾牌）", "example": "Target the chest muscles.", "translation": "针对胸部肌肉。"},
    {"word": "isolate", "wordTranslation": "孤立训练", "phonetic": "/ˈaɪsəleɪt/", "partOfSpeech": "v.", "etymology": "island-岛屿 + -ate", "example": "Isolate the bicep.", "translation": "孤立训练二头肌。"},
    {"word": "compound", "wordTranslation": "复合动作", "phonetic": "/ˈkɒmpaʊnd/", "partOfSpeech": "adj.", "etymology": "com-共同 + pound-放置", "example": "Squats are compound movements.", "translation": "深蹲是复合动作。"},
    {"word": "stabilizer", "wordTranslation": "稳定肌", "phonetic": "/ˈsteɪbəlaɪzər/", "partOfSpeech": "n.", "etymology": "stabil-稳定 + -izer", "example": "Use stabilizer muscles.", "translation": "使用稳定肌。"},
    {"word": "flex", "wordTranslation": "收缩/弯曲", "phonetic": "/fleks/", "partOfSpeech": "v.", "etymology": "来自拉丁语flectere（弯曲）", "example": "Flex your muscles.", "translation": "收缩你的肌肉。"},
    {"word": "contract", "wordTranslation": "收缩", "phonetic": "/kənˈtrækt/", "partOfSpeech": "v.", "etymology": "con-共同 + tract-拉", "example": "Contract the muscle.", "translation": "收缩肌肉。"},
    {"word": "relax", "wordTranslation": "放松", "phonetic": "/rɪˈlæks/", "partOfSpeech": "v.", "etymology": "re-回 + lax-松", "example": "Relax between sets.", "translation": "组间放松。"},
    {"word": "squeeze", "wordTranslation": "挤压", "phonetic": "/skwiːz/", "partOfSpeech": "v.", "etymology": "来自古英语cwosan", "example": "Squeeze at the top.", "translation": "在顶点挤压。"},

    # 健身装备
    {"word": "glove", "wordTranslation": "手套", "phonetic": "/ɡlʌv/", "partOfSpeech": "n.", "etymology": "g-手 + love-爱", "example": "Wear workout gloves.", "translation": "戴训练手套。"},
    {"word": "belt", "wordTranslation": "腰带", "phonetic": "/belt/", "partOfSpeech": "n.", "etymology": "来自古英语belt", "example": "Use a lifting belt.", "translation": "使用举重腰带。"},
    {"word": "wrap", "wordTranslation": "护绷带", "phonetic": "/ræp/", "partOfSpeech": "n.", "etymology": "来自古英语wræp", "example": "Use knee wraps.", "translation": "使用膝盖绷带。"},
    {"word": "strap", "wordTranslation": "绑带", "phonetic": "/stræp/", "partOfSpeech": "n.", "etymology": "来自低地德语strof", "example": "Use lifting straps.", "translation": "使用举重绑带。"},
    {"word": "sleeve", "wordTranslation": "护套", "phonetic": "/sliːv/", "partOfSpeech": "n.", "etymology": "来自古英语slæf", "example": "Wear knee sleeves.", "translation": "戴护膝套。"},
    {"word": "brace", "wordTranslation": "支撑架", "phonetic": "/breɪs/", "partOfSpeech": "n.", "etymology": "来自古法语bracier（拥抱）", "example": "Use a back brace.", "translation": "使用背部支撑架。"},
    {"word": "chalk", "wordTranslation": "镁粉", "phonetic": "/tʃɔːk/", "partOfSpeech": "n.", "etymology": "来自古英语cealc", "example": "Use chalk for grip.", "translation": "用镁粉增加握力。"},
    {"word": "wristband", "wordTranslation": "护腕", "phonetic": "/ˈrɪstbænd/", "partOfSpeech": "n.", "etymology": "wrist-腕 + band-带", "example": "Wear wristbands.", "translation": "戴护腕。"},
    {"word": "headband", "wordTranslation": "头带", "phonetic": "/ˈhedbænd/", "partOfSpeech": "n.", "etymology": "head-头 + band-带", "example": "Wear a headband.", "translation": "带头带。"},
    {"word": "shoes", "wordTranslation": "运动鞋", "phonetic": "/ʃuːz/", "partOfSpeech": "n.", "etymology": "来自古英语sceh", "example": "Buy proper workout shoes.", "translation": "买合适的运动鞋。"},

    # 其他
    {"word": "gym membership", "wordTranslation": "健身房会员", "phonetic": "/dʒɪm ˈmembəʃɪp/", "partOfSpeech": "n.", "etymology": "gym-健身房 + membership-会员", "example": "Cancel gym membership.", "translation": "取消健身房会员。"},
    {"word": "appointment", "wordTranslation": "预约", "phonetic": "/əˈpɔɪntmənt/", "partOfSpeech": "n.", "etymology": "ap-向 + point-点 + -ment", "example": "Book an appointment.", "translation": "预约。"},
    {"word": "sanitizer", "wordTranslation": "消毒剂", "phonetic": "/sænɪˈtaɪzər/", "partOfSpeech": "n.", "etymology": "sanit-卫生 + -izer", "example": "Use hand sanitizer.", "translation": "使用洗手液。"},
    {"word": "towel", "wordTranslation": "毛巾", "phonetic": "/ˈtaʊəl/", "partOfSpeech": "n.", "etymology": "来自古法语toaille", "example": "Bring a towel.", "translation": "带毛巾。"},
    {"word": "locker", "wordTranslation": "储物柜", "phonetic": "/ˈlɒkər/", "partOfSpeech": "n.", "etymology": "lock-锁 + -er", "example": "Use the locker room.", "translation": "用更衣室。"},
    {"word": "motivation", "wordTranslation": "动力", "phonetic": "/ˌməʊtɪˈveɪʃən/", "partOfSpeech": "n.", "etymology": "mot-动 + -ivation", "example": "Stay motivated.", "translation": "保持动力。"},
    {"word": "discipline", "wordTranslation": "自律", "phonetic": "/ˈdɪsɪplɪn/", "partOfSpeech": "n.", "etymology": "disciple-门徒 + -ine", "example": "Fitness requires discipline.", "translation": "健身需要自律。"},
    {"word": "consistency", "wordTranslation": "坚持/一致性", "phonetic": "/kənˈsɪstənsi/", "partOfSpeech": "n.", "etymology": "con-共同 + sist-站 + -ency", "example": "Be consistent.", "translation": "要坚持。"},
    {"word": "dedication", "wordTranslation": "奉献/投入", "phonetic": "/ˌdedɪˈkeɪʃən/", "partOfSpeech": "n.", "etymology": "de-完全 + dic-说 + -ation", "example": "Dedication pays off.", "translation": "付出总有回报。"},
    {"word": "determination", "wordTranslation": "决心", "phonetic": "/dɪˌtɜːmɪˈneɪʃən/", "partOfSpeech": "n.", "etymology": "de-完全 + term-边界 + -ation", "example": "Show determination.", "translation": "展现决心。"},
]

for w in words:
    note = genanki.Note(
        model=my_model,
        fields=[w['word'], w['wordTranslation'], w['phonetic'], w['partOfSpeech'], w['etymology'], w['example'], w['translation']]
    )
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file('/workspace/fitness_vocabulary.apkg')
print(f'fitness_vocabulary.apkg 已生成！共 {len(words)} 个单词')
