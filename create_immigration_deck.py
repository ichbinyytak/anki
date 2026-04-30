import genanki

my_model = genanki.Model(
    1234567890,
    'Immigration Dictionary Model',
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

deck = genanki.Deck(9876543210, 'Immigration Vocabulary')

words = [
    # 移民签证基础词汇
    {"word": "immigration", "wordTranslation": "移民", "phonetic": "/ˌɪmɪˈɡreɪʃən/", "partOfSpeech": "n.", "etymology": "im-进入 + migr-迁移 + -ation", "example": "Immigration policies vary by country.", "translation": "各国的移民政策各不相同。"},
    {"word": "emigration", "wordTranslation": "移居外国", "phonetic": "/ˌemɪˈɡreɪʃən/", "partOfSpeech": "n.", "etymology": "e-出 + migr-迁移 + -ation", "example": "Emigration rates have increased this year.", "translation": "今年的移居外国比率增加了。"},
    {"word": "visa", "wordTranslation": "签证", "phonetic": "/ˈviːzə/", "partOfSpeech": "n.", "etymology": "来自拉丁语visa（被看过的）", "example": "You need a valid visa to enter the country.", "translation": "你需要有效签证才能进入该国。"},
    {"word": "passport", "wordTranslation": "护照", "phonetic": "/ˈpæspɔːt/", "partOfSpeech": "n.", "etymology": "pass-通过 + port-港口", "example": "Please show your passport at the border.", "translation": "请在边境出示您的护照。"},
    {"word": "citizenship", "wordTranslation": "国籍/公民身份", "phonetic": "/ˈsɪtɪzənʃɪp/", "partOfSpeech": "n.", "etymology": "citizen-公民 + -ship身份", "example": "She obtained citizenship after five years.", "translation": "五年后她获得了国籍。"},
    {"word": "naturalization", "wordTranslation": "归化/入籍", "phonetic": "/ˌnætʃərəlaɪˈzeɪʃən/", "partOfSpeech": "n.", "etymology": "nature-自然 + -ization过程", "example": "Naturalization requires passing a test.", "translation": "归化需要通过考试。"},
    {"word": "resident", "wordTranslation": "居民", "phonetic": "/ˈrezɪdənt/", "partOfSpeech": "n.", "etymology": "re-再 + sid-坐 + -ent", "example": "He is a permanent resident of the US.", "translation": "他是美国的永久居民。"},
    {"word": "alien", "wordTranslation": "外国人/外星人", "phonetic": "/ˈeɪliən/", "partOfSpeech": "n.", "etymology": "来自拉丁语alienus（属于别人的）", "example": "An illegal alien was detained at the border.", "translation": "一名非法外国人被扣押在边境。"},
    {"word": "native", "wordTranslation": "本地人/土著", "phonetic": "/ˈneɪtɪv/", "partOfSpeech": "n./adj.", "etymology": "nat-出生 + -ive", "example": "She is a native speaker of English.", "translation": "她是英语母语者。"},
    {"word": "status", "wordTranslation": "身份/地位", "phonetic": "/ˈsteɪtəs/", "partOfSpeech": "n.", "etymology": "来自拉丁语status（状态）", "example": "What is your immigration status?", "translation": "你的移民身份是什么？"},

    # F4签证相关
    {"word": "family-based", "wordTranslation": "基于家庭的", "phonetic": "/ˈfæməli beɪst/", "partOfSpeech": "adj.", "etymology": "family-家庭 + based-基于", "example": "Family-based immigration is common.", "translation": "家庭移民很常见。"},
    {"word": "sibling", "wordTranslation": "兄弟姐妹", "phonetic": "/ˈsɪblɪŋ/", "partOfSpeech": "n.", "etymology": "sib-亲属 + -ling小", "example": "I sponsored my sibling for immigration.", "translation": "我为我的兄弟姐妹担保移民。"},
    {"word": "petitioner", "wordTranslation": "请愿人/申请人", "phonetic": "/pəˈtɪʃənər/", "partOfSpeech": "n.", "etymology": "petition-请愿 + -er人", "example": "The petitioner must be a US citizen.", "translation": "申请人必须是美国公民。"},
    {"word": "beneficiary", "wordTranslation": "受益人", "phonetic": "/ˌbenɪˈfɪʃieri/", "partOfSpeech": "n.", "etymology": "bene-好 + fic-做 + -iary", "example": "The beneficiary will receive the visa.", "translation": "受益人将获得签证。"},
    {"word": "sponsor", "wordTranslation": "担保人", "phonetic": "/ˈspɒnsər/", "partOfSpeech": "n.", "etymology": "spons-承诺 + -or人", "example": "You need a sponsor for the application.", "translation": "申请需要担保人。"},
    {"word": "affidavit", "wordTranslation": "宣誓书", "phonetic": "/ˌæfɪˈdeɪvɪt/", "partOfSpeech": "n.", "etymology": "af-向 + fid-信任 + -avit", "example": "Please sign the affidavit of support.", "translation": "请签署经济担保宣誓书。"},
    {"word": "petition", "wordTranslation": "请愿/申请", "phonetic": "/pəˈtɪʃən/", "partOfSpeech": "n.", "etymology": "pet-寻求 + -ition", "example": "File the petition with USCIS.", "translation": "向移民局提交申请。"},
    {"word": "priority date", "wordTranslation": "优先日期", "phonetic": "/praɪˈɒrəti deɪt/", "partOfSpeech": "n.", "etymology": "priority-优先 + date-日期", "example": "Your priority date determines your place in line.", "translation": "优先日期决定你的排队顺序。"},
    {"word": "visa bulletin", "wordTranslation": "签证公告", "phonetic": "/ˈviːzə bʊlətɪn/", "partOfSpeech": "n.", "etymology": "visa-签证 + bulletin-公告", "example": "Check the monthly visa bulletin.", "translation": "查看每月的签证公告。"},
    {"word": "current", "wordTranslation": "当前的/流行的", "phonetic": "/ˈkʌrənt/", "partOfSpeech": "adj.", "etymology": "cur-跑 + -ent", "example": "The visa is now current.", "translation": "签证现在有名额了。"},

    # 移民局相关
    {"word": "USCIS", "wordTranslation": "美国公民及移民服务局", "phonetic": "/juː-es-aɪ-es/", "partOfSpeech": "abbr.", "etymology": "United States Citizenship and Immigration Services", "example": "File your forms with USCIS.", "translation": "向移民局提交您的表格。"},
    {"word": "Department of State", "wordTranslation": "国务院", "phonetic": "/dɪˈpɑːtmənt əv steɪt/", "partOfSpeech": "n.", "etymology": "department-部门 + state-国家", "example": "The State Department processes visas.", "translation": "国务院处理签证事务。"},
    {"word": "consulate", "wordTranslation": "领事馆", "phonetic": "/ˈkɒnsjʊlət/", "partOfSpeech": "n.", "etymology": "consul-领事 + -ate", "example": "Visit the US consulate for interview.", "translation": "去美国领事馆面试。"},
    {"word": "embassy", "wordTranslation": "大使馆", "phonetic": "/ˈembəsi/", "partOfSpeech": "n.", "etymology": "ambassador-大使 + -y", "example": "The embassy is in the capital city.", "translation": "大使馆在首都。"},
    {"word": "immigration officer", "wordTranslation": "移民官", "phonetic": "/ˌɪmɪˈɡreɪʃən ˈɒfɪsər/", "partOfSpeech": "n.", "etymology": "immigration-移民 + officer-官员", "example": "The immigration officer approved my entry.", "translation": "移民官批准了我的入境。"},
    {"word": "NVC", "wordTranslation": "国家签证中心", "phonetic": "/en-viː-siː/", "partOfSpeech": "abbr.", "etymology": "National Visa Center", "example": "NVC will process your documents.", "translation": "国家签证中心将处理您的文件。"},

    # 表格和文件
    {"word": "form", "wordTranslation": "表格", "phonetic": "/fɔːm/", "partOfSpeech": "n.", "etymology": "来自拉丁语forma（形状）", "example": "Fill out this form completely.", "translation": "请完整填写此表格。"},
    {"word": "application", "wordTranslation": "申请", "phonetic": "/ˌæplɪˈkeɪʃən/", "partOfSpeech": "n.", "etymology": "ap-向 + plic-折叠 + -ation", "example": "Submit your application online.", "translation": "在线提交您的申请。"},
    {"word": "documentation", "wordTranslation": "文件/文档", "phonetic": "/ˌdɒkjʊmenˈteɪʃən/", "partOfSpeech": "n.", "etymology": "document-文件 + -ation", "example": "Gather all required documentation.", "translation": "收集所有需要的文件。"},
    {"word": "certificate", "wordTranslation": "证书", "phonetic": "/səˈtɪfɪkɪt/", "partOfSpeech": "n.", "etymology": "cert-确认 + -fic + -ate", "example": "Provide your birth certificate.", "translation": "提供您的出生证明。"},
    {"word": "birth certificate", "wordTranslation": "出生证明", "phonetic": "/bɜːθ səˈtɪfɪkɪt/", "partOfSpeech": "n.", "etymology": "birth-出生 + certificate-证书", "example": "You need a birth certificate.", "translation": "你需要出生证明。"},
    {"word": "marriage certificate", "wordTranslation": "结婚证", "phonetic": "/ˈmærɪdʒ səˈtɪfɪkɪt/", "partOfSpeech": "n.", "etymology": "marriage-婚姻 + certificate-证书", "example": "Submit your marriage certificate.", "translation": "提交您的结婚证。"},
    {"word": "divorce decree", "wordTranslation": "离婚判决书", "phonetic": "/dɪˈvɔːs ˈdiːkriː/", "partOfSpeech": "n.", "etymology": "divorce-离婚 + decree-判决", "example": "Provide the divorce decree if applicable.", "translation": "如适用，提供离婚判决书。"},
    {"word": "police clearance", "wordTranslation": "无犯罪记录证明", "phonetic": "/pəˈliːs ˈklɪərəns/", "partOfSpeech": "n.", "etymology": "police-警察 + clearance-清除", "example": "Get a police clearance certificate.", "translation": "获取无犯罪记录证明。"},
    {"word": "medical examination", "wordTranslation": "体检", "phonetic": "/ˈmedɪkəl ɪɡˌzæmɪˈneɪʃən/", "partOfSpeech": "n.", "etymology": "medical-医学 + examination-检查", "example": "Complete your medical examination.", "translation": "完成您的体检。"},
    {"word": "vaccination", "wordTranslation": "疫苗接种", "phonetic": "/ˌvæksɪˈneɪʃən/", "partOfSpeech": "n.", "etymology": "vacc-牛痘 + -ation", "example": "Show your vaccination records.", "translation": "出示您的疫苗接种记录。"},
    {"word": "translation", "wordTranslation": "翻译/译文", "phonetic": "/trænsˈleɪʃən/", "partOfSpeech": "n.", "etymology": "trans-转移 + lat-带 + -ion", "example": "Provide certified translation of documents.", "translation": "提供文件的专业翻译件。"},
    {"word": "notarization", "wordTranslation": "公证", "phonetic": "/ˌnəʊtəraɪˈzeɪʃən/", "partOfSpeech": "n.", "etymology": "notar-公证人 + -ization", "example": "All documents need notarization.", "translation": "所有文件都需要公证。"},
    {"word": "authentication", "wordTranslation": "认证", "phonetic": "/ɔːˌθentɪˈkeɪʃən/", "partOfSpeech": "n.", "etymology": "authentic-真实的 + -ation", "example": "Documents require authentication.", "translation": "文件需要认证。"},
    {"word": "apostille", "wordTranslation": "海牙认证", "phonetic": "/əˈpɒstɪl/", "partOfSpeech": "n.", "etymology": "来自法语apostille（批注）", "example": "Get an apostille for your documents.", "translation": "为您的文件办理海牙认证。"},

    # 面试和程序
    {"word": "interview", "wordTranslation": "面试", "phonetic": "/ˈɪntəvjuː/", "partOfSpeech": "n.", "etymology": "inter-之间 + view-看", "example": "Attend your visa interview.", "translation": "参加您的签证面试。"},
    {"word": "fingerprint", "wordTranslation": "指纹", "phonetic": "/ˈfɪŋɡəprɪnt/", "partOfSpeech": "n.", "etymology": "finger-手指 + print-印", "example": "Provide your fingerprints.", "translation": "提供您的指纹。"},
    {"word": "biometrics", "wordTranslation": "生物识别", "phonetic": "/ˌbaɪəˈmetrɪks/", "partOfSpeech": "n.", "etymology": "bio-生物 + metrics-测量", "example": "Submit biometrics at the office.", "translation": "在办公室提交生物识别信息。"},
    {"word": "processing time", "wordTranslation": "处理时间", "phonetic": "/ˈprəʊsesɪŋ taɪm/", "partOfSpeech": "n.", "etymology": "processing-处理 + time-时间", "example": "Check the current processing time.", "translation": "查看当前处理时间。"},
    {"word": "approval", "wordTranslation": "批准", "phonetic": "/əˈpruːvəl/", "partOfSpeech": "n.", "etymology": "ap-向 + prov-测试 + -al", "example": "Wait for visa approval.", "translation": "等待签证批准。"},
    {"word": "denial", "wordTranslation": "拒绝", "phonetic": "/dɪˈnaɪəl/", "partOfSpeech": "n.", "etymology": "deny-否认 + -al", "example": "Appeal the denial of your visa.", "translation": "对签证拒绝提出上诉。"},
    {"word": "appeal", "wordTranslation": "上诉", "phonetic": "/əˈpiːl/", "partOfSpeech": "n.", "etymology": "ap-向 + peal-呼吁", "example": "You can file an appeal.", "translation": "您可以提出上诉。"},
    {"word": "hearing", "wordTranslation": "听证会", "phonetic": "/ˈhɪərɪŋ/", "partOfSpeech": "n.", "etymology": "hear-听 + -ing", "example": "Attend the immigration hearing.", "translation": "参加移民听证会。"},
    {"word": "decision", "wordTranslation": "决定", "phonetic": "/dɪˈsɪʒən/", "partOfSpeech": "n.", "etymology": "de-完全 + cis-切 + -ion", "example": "Wait for the decision.", "translation": "等待决定。"},
    {"word": "notice", "wordTranslation": "通知/ notice", "phonetic": "/ˈnəʊtɪs/", "partOfSpeech": "n.", "etymology": "not-知道 + -ice", "example": "You will receive a notice.", "translation": "您将收到通知。"},

    # 法律和权利
    {"word": "lawful", "wordTranslation": "合法的", "phonetic": "/ˈlɔːfəl/", "partOfSpeech": "adj.", "etymology": "law-法律 + -ful", "example": "Maintain lawful status.", "translation": "保持合法身份。"},
    {"word": "illegal", "wordTranslation": "非法的", "phonetic": "/ɪˈliːɡəl/", "partOfSpeech": "adj.", "etymology": "il-不 + legal-合法的", "example": "Illegal immigration is a crime.", "translation": "非法移民是犯罪行为。"},
    {"word": "deportation", "wordTranslation": "驱逐出境", "phonetic": "/ˌdiːpɔːˈteɪʃən/", "partOfSpeech": "n.", "etymology": "de-离开 + port-携带 + -ation", "example": "Face deportation if caught.", "translation": "被抓将面临驱逐出境。"},
    {"word": "removal", "wordTranslation": "移除/遣返", "phonetic": "/rɪˈmuːvəl/", "partOfSpeech": "n.", "etymology": "re-回 + mov-移动 + -al", "example": "Removal proceedings began.", "translation": "遣返程序开始了。"},
    {"word": "asylum", "wordTranslation": "庇护", "phonetic": "/əˈsaɪləm/", "partOfSpeech": "n.", "etymology": "来自希腊语asylon（避难所）", "example": "Seek asylum in the US.", "translation": "在美国寻求庇护。"},
    {"word": "refugee", "wordTranslation": "难民", "phonetic": "/ˌrefjʊˈdʒiː/", "partOfSpeech": "n.", "etymology": "来自法语refugié（避难者）", "example": "The refugee status was granted.", "translation": "难民身份已获批准。"},
    {"word": "human rights", "wordTranslation": "人权", "phonetic": "/ˈhjuːmən raɪts/", "partOfSpeech": "n.", "etymology": "human-人 + rights-权利", "example": "Human rights must be respected.", "translation": "必须尊重人权。"},
    {"word": "due process", "wordTranslation": "正当程序", "phonetic": "/djuː ˈprəʊses/", "partOfSpeech": "n.", "etymology": "due-应得的 + process-程序", "example": "Everyone deserves due process.", "translation": "每个人都应享有正当程序。"},
    {"word": "attorney", "wordTranslation": "律师", "phonetic": "/əˈtɜːni/", "partOfSpeech": "n.", "etymology": "at-向 + torn-转 + -ey", "example": "Hire an immigration attorney.", "translation": "聘请移民律师。"},
    {"word": "legal representation", "wordTranslation": "法律代理", "phonetic": "/ˈliːɡəl ˌreprɪzenˈteɪʃən/", "partOfSpeech": "n.", "etymology": "legal-法律的 + representation-代表", "example": "Get legal representation.", "translation": "获得法律代理。"},

    # 时间和期限
    {"word": "deadline", "wordTranslation": "截止日期", "phonetic": "/ˈdedlaɪn/", "partOfSpeech": "n.", "etymology": "dead-死 + line-线", "example": "Meet the submission deadline.", "translation": "在截止日期前提交。"},
    {"word": "extension", "wordTranslation": "延期", "phonetic": "/ɪkˈstenʃən/", "partOfSpeech": "n.", "etymology": "ex-出 + tens-伸 + -ion", "example": "Request an extension.", "translation": "请求延期。"},
    {"word": "valid", "wordTranslation": "有效的", "phonetic": "/ˈvælɪd/", "partOfSpeech": "adj.", "etymology": "val-价值 + -id", "example": "Your visa must be valid.", "translation": "您的签证必须有效。"},
    {"word": "expire", "wordTranslation": "过期", "phonetic": "/ɪkˈspaɪər/", "partOfSpeech": "v.", "etymology": "ex-出 + pir-呼吸", "example": "Don't let your visa expire.", "translation": "不要让您的签证过期。"},
    {"word": "renewal", "wordTranslation": "续期", "phonetic": "/rɪˈnjuːəl/", "partOfSpeech": "n.", "etymology": "re-再 + new-新 + -al", "example": "Apply for renewal early.", "translation": "提前申请续期。"},
    {"word": "duration", "wordTranslation": "持续时间", "phonetic": "/djʊˈreɪʃən/", "partOfSpeech": "n.", "etymology": "dur-持续 + -ation", "example": "What is the duration of stay?", "translation": "停留时间是多久？"},
    {"word": "grace period", "wordTranslation": "宽限期", "phonetic": "/ɡreɪs ˈpɪəriəd/", "partOfSpeech": "n.", "etymology": "grace-恩惠 + period-期间", "example": "You have a 10-day grace period.", "translation": "你有10天宽限期。"},

    # 费用和财务
    {"word": "fee", "wordTranslation": "费用", "phonetic": "/fiː/", "partOfSpeech": "n.", "etymology": "来自拉丁语fides（信任）", "example": "Pay the filing fee.", "translation": "支付申请费。"},
    {"word": "processing fee", "wordTranslation": "处理费", "phonetic": "/ˈprəʊsesɪŋ fiː/", "partOfSpeech": "n.", "etymology": "processing-处理 + fee-费用", "example": "The processing fee is non-refundable.", "translation": "处理费不可退还。"},
    {"word": "financial support", "wordTranslation": "经济支持", "phonetic": "/faɪˈnænʃəl səˈpɔːt/", "partOfSpeech": "n.", "etymology": "financial-财务的 + support-支持", "example": "Prove financial support.", "translation": "证明经济支持能力。"},
    {"word": "income", "wordTranslation": "收入", "phonetic": "/ˈɪnkʌm/", "partOfSpeech": "n.", "etymology": "in-进入 + com-来", "example": "Show your annual income.", "translation": "出示您的年收入。"},
    {"word": "tax return", "wordTranslation": "纳税申报", "phonetic": "/tæks rɪˈtɜːn/", "partOfSpeech": "n.", "etymology": "tax-税 + return-返回", "example": "Submit tax returns for three years.", "translation": "提交三年的纳税申报。"},
    {"word": "affidavit of support", "wordTranslation": "经济担保书", "phonetic": "/ˌæfɪˈdeɪvɪt əv səˈpɔːt/", "partOfSpeech": "n.", "etymology": "affidavit-宣誓书 + support-支持", "example": "Sign the affidavit of support.", "translation": "签署经济担保书。"},
    {"word": "sponsor's income", "wordTranslation": "担保人收入", "phonetic": "/ˈspɒnsərz ˈɪnkʌm/", "partOfSpeech": "n.", "etymology": "sponsor-担保人 + income-收入", "example": "The sponsor's income must meet the threshold.", "translation": "担保人收入必须达到门槛。"},

    # 亲属关系
    {"word": "immediate relative", "wordTranslation": "直系亲属", "phonetic": "/ɪˈmiːdiət ˈrelətɪv/", "partOfSpeech": "n.", "etymology": "immediate-直接的 + relative-亲属", "example": "Immediate relatives have priority.", "translation": "直系亲属有优先权。"},
    {"word": "parent", "wordTranslation": "父母", "phonetic": "/ˈpeərənt/", "partOfSpeech": "n.", "etymology": "par-生产 + -ent", "example": "A US citizen can petition for parents.", "translation": "美国公民可以为父母申请。"},
    {"word": "child", "wordTranslation": "孩子", "phonetic": "/tʃaɪld/", "partOfSpeech": "n.", "etymology": "来自古英语cild", "example": "Bring your children's documents.", "translation": "带上您孩子的文件。"},
    {"word": "spouse", "wordTranslation": "配偶", "phonetic": "/spaʊs/", "partOfSpeech": "n.", "etymology": "来自拉丁语sponsus（订婚的）", "example": "Include your spouse in the application.", "translation": "在申请中包含您的配偶。"},
    {"word": "dependent", "wordTranslation": "被抚养人", "phonetic": "/dɪˈpendənt/", "partOfSpeech": "n.", "etymology": "de-下 + pend-挂 + -ent", "example": "List all dependents.", "translation": "列出所有被抚养人。"},
    {"word": "family member", "wordTranslation": "家庭成员", "phonetic": "/ˈfæməli ˈmembər/", "partOfSpeech": "n.", "etymology": "family-家庭 + member-成员", "example": "All family members must be listed.", "translation": "所有家庭成员都必须列出。"},
    {"word": "relationship", "wordTranslation": "关系", "phonetic": "/rɪˈleɪʃənʃɪp/", "partOfSpeech": "n.", "etymology": "re-回 + lat-带 + -ion + -ship", "example": "Prove your relationship.", "translation": "证明你们的关系。"},
    {"word": "household", "wordTranslation": "家庭/ household", "phonetic": "/ˈhaʊshəʊld/", "partOfSpeech": "n.", "etymology": "house-房子 + hold-拥有", "example": "How many in your household?", "translation": "您家里有多少人？"},

    # 居住和工作
    {"word": "address", "wordTranslation": "地址", "phonetic": "/əˈdres/", "partOfSpeech": "n.", "etymology": "ad-向 + dress-指导", "example": "Update your address.", "translation": "更新您的地址。"},
    {"word": "residence", "wordTranslation": "居住地", "phonetic": "/ˈrezɪdəns/", "partOfSpeech": "n.", "etymology": "re-再 + sid-坐 + -ence", "example": "Change your residence address.", "translation": "更改居住地址。"},
    {"word": "domicile", "wordTranslation": "户籍/永久居住地", "phonetic": "/ˈdɒmɪsaɪl/", "partOfSpeech": "n.", "etymology": "dom-家 + -ic + -ile", "example": "Your domicile determines jurisdiction.", "translation": "您的户籍决定管辖权。"},
    {"word": "employment", "wordTranslation": "就业", "phonetic": "/ɪmˈplɔɪmənt/", "partOfSpeech": "n.", "etymology": "em-进入 + ploy-用 + -ment", "example": "Employment authorization is needed.", "translation": "需要就业授权。"},
    {"word": "work permit", "wordTranslation": "工作许可证", "phonetic": "/wɜːk ˈpɜːmɪt/", "partOfSpeech": "n.", "etymology": "work-工作 + permit-许可", "example": "Apply for a work permit.", "translation": "申请工作许可证。"},
    {"word": "social security", "wordTranslation": "社会保障", "phonetic": "/ˈsəʊʃəl sɪˈkjʊərɪti/", "partOfSpeech": "n.", "etymology": "social-社会的 + security-安全", "example": "Get a social security number.", "translation": "获取社会安全号码。"},
    {"word": "tax ID", "wordTranslation": "税号", "phonetic": "/tæks aɪ-diː/", "partOfSpeech": "n.", "etymology": "tax-税 + ID-身份", "example": "You need a tax ID number.", "translation": "您需要税号。"},

    # 面试常见问题
    {"word": "purpose", "wordTranslation": "目的", "phonetic": "/ˈpɜːpəs/", "partOfSpeech": "n.", "etymology": "pur-向前 + pos-放置", "example": "What is your purpose of visit?", "translation": "您访问的目的是什么？"},
    {"word": "itinerary", "wordTranslation": "行程", "phonetic": "/aɪˈtɪnərəri/", "partOfSpeech": "n.", "etymology": "it-走 + in-在 + -erary", "example": "Present your travel itinerary.", "translation": "出示您的旅行行程。"},
    {"word": "accommodation", "wordTranslation": "住宿", "phonetic": "/əˌkɒməˈdeɪʃən/", "partOfSpeech": "n.", "etymology": "ac-向 + mod-方式 + -ation", "example": "Where will you stay?", "translation": "您将住在哪里？"},
    {"word": "duration of stay", "wordTranslation": "停留时间", "phonetic": "/djʊˈreɪʃən əv steɪ/", "partOfSpeech": "n.", "etymology": "duration-持续时间 + stay-停留", "example": "How long is your duration of stay?", "translation": "您要停留多久？"},
    {"word": "ties", "wordTranslation": "联系/纽带", "phonetic": "/taɪz/", "partOfSpeech": "n.", "etymology": "tie-系 + -s复数", "example": "Show strong ties to your home country.", "translation": "展示您与祖国的紧密联系。"},
    {"word": "intention", "wordTranslation": "意图", "phonetic": "/ɪnˈtenʃən/", "partOfSpeech": "n.", "etymology": "in-向 + tent-伸 + -ion", "example": "State your intention clearly.", "translation": "清楚地说明您的意图。"},

    # 状态和结果
    {"word": "pending", "wordTranslation": "待定/处理中", "phonetic": "/ˈpendɪŋ/", "partOfSpeech": "adj.", "etymology": "pend-挂 + -ing", "example": "Your case is still pending.", "translation": "您的案件仍在处理中。"},
    {"word": "approved", "wordTranslation": "已批准", "phonetic": "/əˈpruːvd/", "partOfSpeech": "adj.", "etymology": "ap-向 + prov-测试 + -ed", "example": "Your visa is approved.", "translation": "您的签证已批准。"},
    {"word": "rejected", "wordTranslation": "被拒绝", "phonetic": "/rɪˈdʒektɪd/", "partOfSpeech": "adj.", "etymology": "re-回 + ject-扔 + -ed", "example": "Your application was rejected.", "translation": "您的申请被拒绝了。"},
    {"word": "withdrawn", "wordTranslation": "撤回", "phonetic": "/wɪðˈdrɔːn/", "partOfSpeech": "adj.", "etymology": "with-回 + draw-拉 + -n", "example": "The petition was withdrawn.", "translation": "申请已被撤回。"},
    {"word": "receipt", "wordTranslation": "收据", "phonetic": "/rɪˈsiːt/", "partOfSpeech": "n.", "etymology": "re-回 + ceipt-拿", "example": "Keep your receipt.", "translation": "保留您的收据。"},
    {"word": "confirmation", "wordTranslation": "确认", "phonetic": "/ˌkɒnfəˈmeɪʃən/", "partOfSpeech": "n.", "etymology": "con-完全 + firm-坚固 + -ation", "example": "You will receive a confirmation.", "translation": "您将收到确认。"},

    # 常见词汇
    {"word": "adjustment", "wordTranslation": "调整/身份调整", "phonetic": "/əˈdʒʌstmənt/", "partOfSpeech": "n.", "etymology": "ad-向 + just-正 + -ment", "example": "Apply for adjustment of status.", "translation": "申请身份调整。"},
    {"word": "consular processing", "wordTranslation": "领事处理", "phonetic": "/ˈkɒnsjʊlə ˈprəʊsesɪŋ/", "partOfSpeech": "n.", "etymology": "consular-领事的 + processing-处理", "example": "Consular processing is required.", "translation": "需要领事处理。"},
    {"word": "labor certification", "wordTranslation": "劳工认证", "phonetic": "/ˈleɪbə ˌsɜːtɪfɪˈkeɪʃən/", "partOfSpeech": "n.", "etymology": "labor-劳工 + certification-认证", "example": "Labor certification is required.", "translation": "需要劳工认证。"},
    {"word": "quota", "wordTranslation": "配额", "phonetic": "/ˈkwəʊtə/", "partOfSpeech": "n.", "etymology": "来自拉丁语quota（多少）", "example": "The annual quota is filled.", "translation": "年度配额已满。"},
    {"word": "retrogression", "wordTranslation": "倒退", "phonetic": "/ˌ retrəˈɡreʃən/", "partOfSpeech": "n.", "etymology": "retro-向后 + gress-走 + -ion", "example": "Visa dates retrogressed.", "translation": "签证日期倒退了。"},
    {"word": "availability", "wordTranslation": "可用性/名额", "phonetic": "/əˌveɪləˈbɪləti/", "partOfSpeech": "n.", "etymology": "avail-有用 + -ability", "example": "Check visa availability.", "translation": "检查签证名额。"},
    {"word": "derivative", "wordTranslation": "衍生的", "phonetic": "/dɪˈrɪvətɪv/", "partOfSpeech": "adj.", "etymology": "de-向下 + riv-河 + -ative", "example": "Derivative beneficiaries include children.", "translation": "衍生受益人包括子女。"},

    # 更多常用词汇
    {"word": "beneficial", "wordTranslation": "有益的/受益的", "phonetic": "/ˌbenɪˈfɪʃəl/", "partOfSpeech": "adj.", "etymology": "bene-好 + fic-做 + -ial", "example": "The immigration is beneficial.", "translation": "移民是有益的。"},
    {"word": "eligible", "wordTranslation": "符合条件的", "phonetic": "/ˈelɪdʒɪbəl/", "partOfSpeech": "adj.", "etymology": "e-出 + lig-选 + -ible", "example": "Are you eligible for this visa?", "translation": "您符合这个签证的条件吗？"},
    {"word": "qualify", "wordTranslation": "符合条件", "phonetic": "/ˈkwɒlɪfaɪ/", "partOfSpeech": "v.", "etymology": "qual-质量 + -ify", "example": "You must qualify for the visa.", "translation": "您必须符合签证条件。"},
    {"word": "requirement", "wordTranslation": "要求", "phonetic": "/rɪˈkwaɪəmənt/", "partOfSpeech": "n.", "etymology": "re-再 + quire-寻求 + -ment", "example": "Meet all requirements.", "translation": "满足所有要求。"},
    {"word": "submit", "wordTranslation": "提交", "phonetic": "/səbˈmɪt/", "partOfSpeech": "v.", "etymology": "sub-下 + mit-送", "example": "Submit your documents.", "translation": "提交您的文件。"},
    {"word": "provide", "wordTranslation": "提供", "phonetic": "/prəˈvaɪd/", "partOfSpeech": "v.", "etymology": "pro-向前 + vid-看", "example": "Provide all necessary documents.", "translation": "提供所有必要的文件。"},
    {"word": "obtain", "wordTranslation": "获得", "phonetic": "/əbˈteɪn/", "partOfSpeech": "v.", "etymology": "ob-向 + tain-拿", "example": "Obtain a visa first.", "translation": "首先获得签证。"},
    {"word": "maintain", "wordTranslation": "保持/维持", "phonetic": "/meɪnˈteɪn/", "partOfSpeech": "v.", "etymology": "main-手 + tain-拿", "example": "Maintain your legal status.", "translation": "保持您的合法身份。"},
    {"word": "comply", "wordTranslation": "遵守", "phonetic": "/kəmˈplaɪ/", "partOfSpeech": "v.", "etymology": "com-共同 + ply-填满", "example": "Comply with immigration laws.", "translation": "遵守移民法。"},
    {"word": "verify", "wordTranslation": "验证", "phonetic": "/ˈverɪfaɪ/", "partOfSpeech": "v.", "etymology": "ver-真实 + -ify", "example": "Verify your information.", "translation": "验证您的信息。"},

    # 状态词汇
    {"word": "expedited", "wordTranslation": "加速的", "phonetic": "/ɪkˈspiːdɪtɪd/", "partOfSpeech": "adj.", "etymology": "ex-出 + ped-脚 + -ed", "example": "Expedited processing is available.", "translation": "可以申请加急处理。"},
    {"word": "premium", "wordTranslation": "优质的/加急的", "phonetic": "/ˈpriːmiəm/", "partOfSpeech": "adj.", "etymology": "pre-前 + em-拿 + -ium", "example": "Premium processing takes 15 days.", "translation": "加急处理需要15天。"},
    {"word": "transfer", "wordTranslation": "转移", "phonetic": "/trænsˈfɜːr/", "partOfSpeech": "n.", "etymology": "trans-穿过 + fer-携带", "example": "Request a case transfer.", "translation": "请求案件转移。"},
    {"word": "jurisdiction", "wordTranslation": "管辖权", "phonetic": "/ˌdʒʊərɪsˈdɪkʃən/", "partOfSpeech": "n.", "etymology": "juris-法律 + dict-说 + -ion", "example": "This office has jurisdiction.", "translation": "这个办公室有管辖权。"},
    {"word": "correspondence", "wordTranslation": "信函/通信", "phonetic": "/ˌkɒrɪˈspɒndəns/", "partOfSpeech": "n.", "etymology": "cor-共同 + respond-响应 + -ence", "example": "Check your correspondence regularly.", "translation": "定期查看您的信函。"},
    {"word": "inquiry", "wordTranslation": "询问", "phonetic": "/ɪnˈkwaɪəri/", "partOfSpeech": "n.", "etymology": "in-向 + quire-寻求", "example": "Send an inquiry about your case.", "translation": "发送关于您案件的询问。"},

    # 法庭和程序
    {"word": "immigration court", "wordTranslation": "移民法庭", "phonetic": "/ˌɪmɪˈɡreɪʃən kɔːt/", "partOfSpeech": "n.", "etymology": "immigration-移民 + court-法庭", "example": "Appear in immigration court.", "translation": "在移民法庭出庭。"},
    {"word": "judge", "wordTranslation": "法官", "phonetic": "/dʒʌdʒ/", "partOfSpeech": "n.", "etymology": "来自拉丁语judex（裁判）", "example": "The judge will decide your case.", "translation": "法官将决定您的案件。"},
    {"word": "bond", "wordTranslation": "保释金", "phonetic": "/bɒnd/", "partOfSpeech": "n.", "etymology": "来自古法语bond（束缚）", "example": "Post a bond for release.", "translation": "缴纳保释金以获释。"},
    {"word": "detention", "wordTranslation": "拘留", "phonetic": "/dɪˈtenʃən/", "partOfSpeech": "n.", "etymology": "de-下 + tent-握 + -ion", "example": "Avoid detention if possible.", "translation": "如果可能的话避免拘留。"},
    {"word": "release", "wordTranslation": "释放", "phonetic": "/rɪˈliːs/", "partOfSpeech": "n.", "etymology": "re-回 + lease-放", "example": "Request release on bond.", "translation": "请求以保释金释放。"},
    {"word": "warrant", "wordTranslation": "逮捕令", "phonetic": "/ˈwɒrənt/", "partOfSpeech": "n.", "etymology": "war-保护 + -ant", "example": "A warrant was issued for arrest.", "translation": "已发出逮捕令。"},

    # 其他重要词汇
    {"word": "amendment", "wordTranslation": "修正/更改", "phonetic": "/əˈmendmənt/", "partOfSpeech": "n.", "etymology": "a-向 + mend-改正 + -ment", "example": "File an amendment to your application.", "translation": "提交申请更正。"},
    {"word": "supplemental", "wordTranslation": "补充的", "phonetic": "/ˌsʌplɪˈmentl/", "partOfSpeech": "adj.", "etymology": "sup-下 + ple-填满 + -mental", "example": "Provide supplemental evidence.", "translation": "提供补充证据。"},
    {"word": "rfe", "wordTranslation": "要求补充材料", "phonetic": "/ɑːr-ef-iː/", "partOfSpeech": "abbr.", "etymology": "Request for Evidence", "example": "Respond to the RFE promptly.", "translation": "及时回复补充材料要求。"},
    {"word": "noa", "wordTranslation": "受理通知", "phonetic": "/en-əʊ-eɪ/", "partOfSpeech": "abbr.", "etymology": "Notice of Action", "example": "Check your NOA for updates.", "translation": "查看您的受理通知获取更新。"},
    {"word": "receipt number", "wordTranslation": "收据号码", "phonetic": "/rɪˈsiːt ˈnʌmbər/", "partOfSpeech": "n.", "etymology": "receipt-收据 + number-号码", "example": "Track your case with receipt number.", "translation": "用收据号码追踪您的案件。"},
    {"word": "case status", "wordTranslation": "案件状态", "phonetic": "/keɪs ˈsteɪtəs/", "partOfSpeech": "n.", "etymology": "case-案件 + status-状态", "example": "Check your case status online.", "translation": "在线查看您的案件状态。"},
    {"word": "inadmissible", "wordTranslation": "不可入境的", "phonetic": "/ˌɪnədˈmɪsɪbəl/", "partOfSpeech": "adj.", "etymology": "in-不 + admissible-可接受的", "example": " grounds for inadmissibility.", "translation": "不可入境的理由。"},
    {"word": "waiver", "wordTranslation": "豁免", "phonetic": "/ˈweɪvər/", "partOfSpeech": "n.", "etymology": "waive-放弃 + -er", "example": "Apply for a waiver of inadmissibility.", "translation": "申请不可入境豁免。"},
    {"word": "abandonment", "wordTranslation": "放弃/遗弃", "phonetic": "/əˈbændənmənt/", "partOfSpeech": "n.", "etymology": "abandon-放弃 + -ment", "example": "Avoid abandonment of application.", "translation": "避免放弃申请。"},
    {"word": "accrual", "wordTranslation": "积累", "phonetic": "/əˈkruːəl/", "partOfSpeech": "n.", "etymology": "ac-向 + cru-积累 + -al", "example": "Check your accrual of presence.", "translation": "检查您的在美时间积累。"},
    {"word": "admissible", "wordTranslation": "可入境的", "phonetic": "/ədˈmɪsɪbəl/", "partOfSpeech": "adj.", "etymology": "ad-向 + miss-送 + -ible", "example": "You are admissible to the US.", "translation": "您可以入境美国。"},
    {"word": "allocation", "wordTranslation": "分配/配额", "phonetic": "/ˌæləˈkeɪʃən/", "partOfSpeech": "n.", "etymology": "al-向 + loc-地方 + -ation", "example": "Visa allocation is limited.", "translation": "签证配额有限。"},
    {"word": "amnesty", "wordTranslation": "大赦", "phonetic": "/ˈæmnəsti/", "partOfSpeech": "n.", "etymology": "amnes-遗忘 + -y", "example": "Immigration amnesty was granted.", "translation": "移民大赦被批准。"},
    {"word": "annulment", "wordTranslation": "废除/取消", "phonetic": "/əˈnʌlmənt/", "partOfSpeech": "n.", "etymology": "an-向 + nul-无效 + -ment", "example": "Apply for annulment of visa.", "translation": "申请取消签证。"},
    {"word": "apprehension", "wordTranslation": "逮捕/担忧", "phonetic": "/ˌæprɪˈhenʃən/", "partOfSpeech": "n.", "etymology": "ap-向 + prehens-抓住 + -ion", "example": "Fear apprehension by authorities.", "translation": "担心被当局逮捕。"},
    {"word": "arraignment", "wordTranslation": "提审", "phonetic": "/əˈreɪnmənt/", "partOfSpeech": "n.", "etymology": "ar-向 + rain-判断 + -ment", "example": "The arraignment was scheduled.", "translation": "提审已安排。"},
    {"word": "assessment", "wordTranslation": "评估", "phonetic": "/əˈsesmənt/", "partOfSpeech": "n.", "etymology": "as-向 + sess-坐 + -ment", "example": "Complete your risk assessment.", "translation": "完成您的风险评估。"},
]

for w in words:
    note = genanki.Note(
        model=my_model,
        fields=[w['word'], w['wordTranslation'], w['phonetic'], w['partOfSpeech'], w['etymology'], w['example'], w['translation']]
    )
    deck.add_note(note)

package = genanki.Package(deck)
package.write_to_file('/workspace/immigration_vocabulary.apkg')
print(f'immigration_vocabulary.apkg 已生成！共 {len(words)} 个单词')
