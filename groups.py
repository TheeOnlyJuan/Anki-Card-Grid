import collections

KanjiGroups = collections.namedtuple("KanjiGroups", ["name", "source", "data"])

ignore = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" + \
          "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ" + \
          "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ" + \
          "1234567890１２３４５６７８９０" + \
          "あいうゔえおぁぃぅぇぉかきくけこがぎぐげごさしすせそざじずぜぞ" + \
          "たちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽ" + \
          "まみむめもやゃゆゅよょらりるれろわをんっ" + \
          "アイウヴエオァィゥェォカキクケコガギグゲゴサシスセソザジズゼゾ" + \
          "タチツテトダヂヅデドナニヌネノハヒフヘホバビブベボパピプペポ" + \
          "マミムメモヤャユュヨョラリルレロワヲンッ" + \
          "!\"$%&'()|=~-^@[;:],./`{+*}<>?\\_" + \
          "＠「；：」、。・‘｛＋＊｝＜＞？＼＿！”＃＄％＆’（）｜＝．〜～ー＾ ゙゙゚" + \
          "☆★＊○●◎〇◯“…『』#♪ﾞ〉〈→》《π×"

groups = [
  KanjiGroups("Grade", "https://web.archive.org/web/20170708205442/http://www.mext.go.jp:80/component/a_menu/education/micro_detail/__icsFiles/afieldfile/2017/05/12/1384661_4_2.pdf (pp. 28-29), https://ja.wikipedia.org/w/index.php?title=%E4%BA%BA%E5%90%8D%E7%94%A8%E6%BC%A2%E5%AD%97&oldid=66764047#%E4%BA%BA%E5%90%8D%E7%94%A8%E6%BC%A2%E5%AD%97%E3%81%AE%E4%B8%80%E8%A6%A7", [
    ('Non-Jouyou', ''),
    ('Grade 1', '一右雨円王音下火花貝学気休玉金九空月犬見五口校左三山四子糸字耳七車手十出女小上森人水正生青石赤先千川早草足村大男竹中虫町天田土二日入年白八百文本名木目夕立力林六'),
    ('Grade 2', '引羽雲園遠黄何夏家科歌画会回海絵外角楽活間丸岩顔帰汽記弓牛魚京強教近兄形計元原言古戸午後語交光公工広考行高合国黒今才細作算姉市思止紙寺時自室社弱首秋週春書少場色食心新親図数星晴声西切雪線船前組走多太体台谷知地池茶昼朝長鳥直通弟店点電冬刀東当答頭同道読内南肉馬買売麦半番父風分聞米歩母方北妹毎万明鳴毛門夜野矢友曜用来理里話'),
    ('Grade 3', '悪安暗委意医育員飲院運泳駅央横屋温化荷界開階寒感漢館岸期起客宮急球究級去橋業局曲銀区苦具君係軽決血研県庫湖向幸港号根祭坂皿仕使始指死詩歯事持次式実写者主取守酒受州拾終習集住重宿所暑助勝商昭消章乗植深申真神身進世整昔全想相送息速族他打対待代第題炭短談着柱注丁帳調追定庭笛鉄転登都度島投湯等豆動童農波配倍箱畑発反板悲皮美鼻筆氷表病秒品負部服福物平返勉放味命面問役薬油有由遊予様洋羊葉陽落流旅両緑礼列練路和'),
    ('Grade 4', '愛案以衣位茨印英栄媛塩岡億加果貨課芽賀改械害街各覚潟完官管関観願岐希季旗器機議求泣給挙漁共協鏡競極熊訓軍郡群径景芸欠結建健験固功好香候康佐差菜最埼材崎昨札刷察参産散残氏司試児治滋辞鹿失借種周祝順初松笑唱焼照城縄臣信井成省清静席積折節説浅戦選然争倉巣束側続卒孫帯隊達単置仲沖兆低底的典伝徒努灯働特徳栃奈梨熱念敗梅博阪飯飛必票標不夫付府阜富副兵別辺変便包法望牧末満未民無約勇要養浴利陸良料量輪類令冷例連老労録'),
    ('Grade 5', '圧囲移因永営衛易益液演応往桜可仮価河過快解格確額刊幹慣眼紀基寄規喜技義逆久旧救居許境均禁句型経潔件険検限現減故個護効厚耕航鉱構興講告混査再災妻採際在財罪殺雑酸賛士支史志枝師資飼示似識質舎謝授修述術準序招証象賞条状常情織職制性政勢精製税責績接設絶祖素総造像増則測属率損貸態団断築貯張停提程適統堂銅導得毒独任燃能破犯判版比肥非費備評貧布婦武復複仏粉編弁保墓報豊防貿暴脈務夢迷綿輸余容略留領歴'),
    ('Grade 6', '胃異遺域宇映延沿恩我灰拡革閣割株干巻看簡危机揮貴疑吸供胸郷勤筋系敬警劇激穴券絹権憲源厳己呼誤后孝皇紅降鋼刻穀骨困砂座済裁策冊蚕至私姿視詞誌磁射捨尺若樹収宗就衆従縦縮熟純処署諸除承将傷障蒸針仁垂推寸盛聖誠舌宣専泉洗染銭善奏窓創装層操蔵臓存尊退宅担探誕段暖値宙忠著庁頂腸潮賃痛敵展討党糖届難乳認納脳派拝背肺俳班晩否批秘俵腹奮並陛閉片補暮宝訪亡忘棒枚幕密盟模訳郵優預幼欲翌乱卵覧裏律臨朗論'),
    ('JuniorHS+', '亜哀挨曖握扱宛嵐依威為畏尉萎偉椅彙違維慰緯壱逸芋咽姻淫陰隠韻唄鬱畝浦詠影鋭疫悦越謁閲炎怨宴援煙猿鉛縁艶汚凹押旺欧殴翁奥憶臆虞乙俺卸穏佳苛架華菓渦嫁暇禍靴寡箇稼蚊牙瓦雅餓介戒怪拐悔皆塊楷潰壊懐諧劾崖涯慨蓋該概骸垣柿核殻郭較隔獲嚇穫岳顎掛括喝渇葛滑褐轄且釜鎌刈甘汗缶肝冠陥乾勘患貫喚堪換敢棺款閑勧寛歓監緩憾還環韓艦鑑含玩頑企伎忌奇祈軌既飢鬼亀幾棋棄毀畿輝騎宜偽欺儀戯擬犠菊吉喫詰却脚虐及丘朽臼糾嗅窮巨拒拠虚距御凶叫狂享況峡挟狭恐恭脅矯響驚仰暁凝巾斤菌琴僅緊錦謹襟吟駆惧愚偶遇隅串屈掘窟繰勲薫刑茎契恵啓掲渓蛍傾携継詣慶憬稽憩鶏迎鯨隙撃桁傑肩倹兼剣拳軒圏堅嫌献遣賢謙鍵繭顕懸幻玄弦舷股虎孤弧枯雇誇鼓錮顧互呉娯悟碁勾孔巧甲江坑抗攻更拘肯侯恒洪荒郊貢控梗喉慌硬絞項溝綱酵稿衡購乞拷剛傲豪克酷獄駒込頃昆恨婚痕紺魂墾懇沙唆詐鎖挫采砕宰栽彩斎債催塞歳載剤削柵索酢搾錯咲刹拶撮擦桟惨傘斬暫旨伺刺祉肢施恣脂紫嗣雌摯賜諮侍慈餌璽軸𠮟疾執湿嫉漆芝赦斜煮遮邪蛇酌釈爵寂朱狩殊珠腫趣寿呪需儒囚舟秀臭袖羞愁酬醜蹴襲汁充柔渋銃獣叔淑粛塾俊瞬旬巡盾准殉循潤遵庶緒如叙徐升召匠床抄肖尚昇沼宵症祥称渉紹訟掌晶焦硝粧詔奨詳彰憧衝償礁鐘丈冗浄剰畳壌嬢錠譲醸拭殖飾触嘱辱尻伸芯辛侵津唇娠振浸紳診寝慎審震薪刃尽迅甚陣尋腎須吹炊帥粋衰酔遂睡穂随髄枢崇据杉裾瀬是姓征斉牲凄逝婿誓請醒斥析脊隻惜戚跡籍拙窃摂仙占扇栓旋煎羨腺詮践箋潜遷薦繊鮮禅漸膳繕狙阻租措粗疎訴塑遡礎双壮荘捜挿桑掃曹曽爽喪痩葬僧遭槽踪燥霜騒藻憎贈即促捉俗賊遜汰妥唾堕惰駄耐怠胎泰堆袋逮替滞戴滝択沢卓拓託濯諾濁但脱奪棚誰丹旦胆淡嘆端綻鍛弾壇恥致遅痴稚緻畜逐蓄秩窒嫡抽衷酎鋳駐弔挑彫眺釣貼超跳徴嘲澄聴懲勅捗沈珍朕陳鎮椎墜塚漬坪爪鶴呈廷抵邸亭貞帝訂逓偵堤艇締諦泥摘滴溺迭哲徹撤添塡殿斗吐妬途渡塗賭奴怒到逃倒凍唐桃透悼盗陶塔搭棟痘筒稲踏謄藤闘騰洞胴瞳峠匿督篤凸突屯豚頓貪鈍曇丼那謎鍋軟尼弐匂虹尿妊忍寧捻粘悩濃把覇婆罵杯排廃輩培陪媒賠伯拍泊迫剝舶薄漠縛爆箸肌鉢髪伐抜罰閥氾帆汎伴畔般販斑搬煩頒範繁藩蛮盤妃彼披卑疲被扉碑罷避尾眉微膝肘匹泌姫漂苗描猫浜賓頻敏瓶扶怖附訃赴浮符普腐敷膚賦譜侮舞封伏幅覆払沸紛雰噴墳憤丙併柄塀幣弊蔽餅壁璧癖蔑偏遍哺捕舗募慕簿芳邦奉抱泡胞俸倣峰砲崩蜂飽褒縫乏忙坊妨房肪某冒剖紡傍帽貌膨謀頰朴睦僕墨撲没勃堀奔翻凡盆麻摩磨魔昧埋膜枕又抹慢漫魅岬蜜妙眠矛霧娘冥銘滅免麺茂妄盲耗猛網黙紋冶弥厄躍闇喩愉諭癒唯幽悠湧猶裕雄誘憂融与誉妖庸揚揺溶腰瘍踊窯擁謡抑沃翼拉裸羅雷頼絡酪辣濫藍欄吏痢履璃離慄柳竜粒隆硫侶虜慮了涼猟陵僚寮療瞭糧厘倫隣瑠涙累塁励戻鈴零霊隷齢麗暦劣烈裂恋廉錬呂炉賂露弄郎浪廊楼漏籠麓賄脇惑枠湾腕'),
    ('Jinmeiyou (regular)', '丑丞乃之乎也云亘亙些亦亥亨亮仔伊伍伽佃佑伶侃侑俄俠俣俐倭俱倦倖偲傭儲允兎兜其冴凌凜凛凧凪凰凱函劉劫勁勺勿匁匡廿卜卯卿厨厩叉叡叢叶只吾吞吻哉哨啄哩喬喧喰喋嘩嘉嘗噌噂圃圭坐尭堯坦埴堰堺堵塙壕壬夷奄奎套娃姪姥娩嬉孟宏宋宕宥寅寓寵尖尤屑峨峻崚嵯嵩嶺巌巖巫已巳巴巷巽帖幌幡庄庇庚庵廟廻弘弛彗彦彪彬徠忽怜恢恰恕悌惟惚悉惇惹惺惣慧憐戊或戟托按挺挽掬捲捷捺捧掠揃摑摺撒撰撞播撫擢孜敦斐斡斧斯於旭昂昊昏昌昴晏晃晄晒晋晟晦晨智暉暢曙曝曳朋朔杏杖杜李杭杵杷枇柑柴柘柊柏柾柚桧檜栞桔桂栖桐栗梧梓梢梛梯桶梶椛梁棲椋椀楯楚楕椿楠楓椰楢楊榎樺榊榛槙槇槍槌樫槻樟樋橘樽橙檎檀櫂櫛櫓欣欽歎此殆毅毘毬汀汝汐汲沌沓沫洸洲洵洛浩浬淵淳渚渚淀淋渥渾湘湊湛溢滉溜漱漕漣澪濡瀕灘灸灼烏焰焚煌煤煉熙燕燎燦燭燿爾牒牟牡牽犀狼猪猪獅玖珂珈珊珀玲琢琢琉瑛琥琶琵琳瑚瑞瑶瑳瓜瓢甥甫畠畢疋疏皐皓眸瞥矩砦砥砧硯碓碗碩碧磐磯祇祢禰祐祐祷禱禄祿禎禎禽禾秦秤稀稔稟稜穣穰穹穿窄窪窺竣竪竺竿笈笹笙笠筈筑箕箔篇篠簞簾籾粥粟糊紘紗紐絃紬絆絢綺綜綴緋綾綸縞徽繫繡纂纏羚翔翠耀而耶耽聡肇肋肴胤胡脩腔脹膏臥舜舵芥芹芭芙芦苑茄苔苺茅茉茸茜莞荻莫莉菅菫菖萄菩萌萠萊菱葦葵萱葺萩董葡蓑蒔蒐蒼蒲蒙蓉蓮蔭蔣蔦蓬蔓蕎蕨蕉蕃蕪薙蕾蕗藁薩蘇蘭蝦蝶螺蟬蟹蠟衿袈袴裡裟裳襖訊訣註詢詫誼諏諄諒謂諺讃豹貰賑赳跨蹄蹟輔輯輿轟辰辻迂迄辿迪迦這逞逗逢遥遙遁遼邑祁郁鄭酉醇醐醍醬釉釘釧銑鋒鋸錘錐錆錫鍬鎧閃閏閤阿陀隈隼雀雁雛雫霞靖鞄鞍鞘鞠鞭頁頌頗顚颯饗馨馴馳駕駿驍魁魯鮎鯉鯛鰯鱒鱗鳩鳶鳳鴨鴻鵜鵬鷗鷲鷺鷹麒麟麿黎黛鼎'),
    ('Jinmeiyou (variant)', '亞惡爲逸榮衞謁圓緣薗應櫻奧橫溫價禍悔海壞懷樂渴卷陷寬漢氣祈器僞戲虛峽狹響曉勤謹駈勳薰惠揭鷄藝擊縣儉劍險圈檢顯驗嚴廣恆黃國黑穀碎雜祉視兒濕實社者煮壽收臭從澁獸縱祝暑署緖諸敍將祥涉燒奬條狀乘淨剩疊孃讓釀神眞寢愼盡粹醉穗瀨齊靜攝節專戰纖禪祖壯爭莊搜巢曾裝僧層瘦騷增憎藏贈臟卽帶滯瀧單嘆團彈晝鑄著廳徵聽懲鎭轉傳都嶋燈盜稻德突難拜盃賣梅髮拔繁晚卑祕碑賓敏冨侮福拂佛勉步峯墨飜每萬默埜彌藥與搖樣謠來賴覽欄龍虜凉綠淚壘類禮曆歷練鍊郞朗廊錄'),
  ]),
  KanjiGroups("Kanji Kentei Level", "http://www.kanken.or.jp/kanken/outline/data/outline_degree_national_list.pdf", [
    ('Probably Chinese', ''),
    ('Level 10', '一右雨円王音下火花貝学気休玉金九空月犬見五口校左三山四子糸字耳七車手十出女小上森人水正生青石赤先千川早草足村大男竹中虫町天田土二日入年白八百文本名木目夕立力林六'),
    ('Level 9', '引羽雲園遠黄何夏家科歌画会回海絵外角楽活間丸岩顔帰汽記弓牛魚京強教近兄形計元原言古戸午後語交光公工広考行高合国黒今才細作算姉市思止紙寺時自室社弱首秋週春書少場色食心新親図数星晴声西切雪線船前組走多太体台谷知地池茶昼朝長鳥直通弟店点電冬刀東当答頭同道読内南肉馬買売麦半番父風分聞米歩母方北妹毎万明鳴毛門夜野矢友曜用来理里話'),
    ('Level 8', '悪安暗委意医育員飲院運泳駅央横屋温化荷界開階寒感漢館岸期起客宮急球究級去橋業局曲銀区苦具君係軽決血研県庫湖向幸港号根祭坂皿仕使始指死詩歯事持次式実写者主取守酒受州拾終習集住重宿所暑助勝商昭消章乗植深申真神身進世整昔全想相送息速族他打対待代第題炭短談着柱注丁帳調追定庭笛鉄転登都度島投湯等豆動童農波配倍箱畑発反板悲皮美鼻筆氷表病秒品負部服福物平返勉放味命面問役薬油有由遊予様洋羊葉陽落流旅両緑礼列練路和'),
    ('Level 7', '愛案以位囲胃衣印栄英塩億加果課貨芽改械害街各覚完官管観関願喜器希旗機季紀議救求泣給挙漁競共協鏡極訓軍郡型径景芸欠結健建験固候功好康航告差最菜材昨刷察札殺参散産残司史士氏試児治辞失借種周祝順初唱松焼照省笑象賞信臣成清静席積折節説戦浅選然倉巣争側束続卒孫帯隊達単置仲貯兆腸低停底的典伝徒努灯働堂得特毒熱念敗梅博飯費飛必標票不付夫府副粉兵別変辺便包法望牧末満未脈民無約勇要養浴利陸料良量輪類令例冷歴連労老録'),
    ('Level 6', '圧易移因営永衛液益演往応恩仮価可河過賀解快格確額刊幹慣眼基寄規技義逆久旧居許境興均禁句群経潔件券検険減現限個故護効厚構耕講鉱混査再妻採災際在罪財桜雑賛酸師志支枝資飼似示識質舎謝授修術述準序承招証常情条状織職制勢性政精製税績責接設絶舌銭祖素総像増造則測属損態貸退団断築張提程敵適統導銅徳独任燃能破判版犯比肥非備俵評貧婦富布武復複仏編弁保墓報豊暴貿防務夢迷綿輸余預容率略留領'),
    ('Level 5', '異遺域宇映延沿我灰拡閣革割株巻干看簡危揮机貴疑吸供胸郷勤筋敬系警劇激穴憲権絹厳源呼己誤后孝皇紅鋼降刻穀骨困砂座済裁策冊蚕姿私至視詞誌磁射捨尺若樹収宗就衆従縦縮熟純処署諸除傷将障城蒸針仁垂推寸盛聖誠宣専泉洗染善創奏層操窓装臓蔵存尊宅担探誕暖段値宙忠著庁潮頂賃痛展党糖討届難乳認納脳派俳拝背肺班晩否批秘腹奮並閉陛片補暮宝訪亡忘棒枚幕密盟模訳優郵幼欲翌乱卵覧裏律臨朗論'),
    ('Level 4', '握扱依偉威為維緯違井壱稲芋陰隠影鋭越援煙縁鉛汚奥押沖憶暇箇菓雅介壊戒皆獲較刈乾勧歓汗環甘監鑑含奇幾祈輝鬼儀戯詰却脚丘及朽巨拠距凶叫恐況狂狭響驚仰駆屈掘繰傾恵継迎撃兼剣圏堅肩軒遣玄枯誇鼓互御恒抗攻更稿荒項香豪腰込婚鎖彩歳載剤咲惨伺刺旨紫脂雌執芝斜煮釈寂朱狩趣需秀舟襲柔獣瞬旬盾巡召床沼称紹詳丈畳飾殖触侵寝慎振浸薪震尋尽陣吹澄是姓征跡占扇鮮訴僧燥騒贈即俗耐替拓沢濁脱丹嘆淡端弾恥致遅蓄徴跳沈珍堤抵摘滴添殿吐渡途奴怒倒唐塔桃盗到踏逃透闘胴峠突曇鈍弐悩濃杯輩拍泊薄迫爆髪罰抜搬繁般販範盤彼疲被避尾微匹描浜敏怖敷普浮腐膚賦舞幅払噴柄壁舗捕峰抱砲傍坊帽忙冒肪凡盆慢漫妙眠矛霧娘茂猛網黙紋躍雄与誉溶謡踊翼頼雷絡欄離粒慮療隣涙隷麗齢暦劣烈恋露郎惑腕'),
    ('Level 3', '哀慰詠悦閲宴炎欧殴乙卸穏佳嫁架華餓塊怪悔慨概該穫郭隔岳掛滑冠勘喚換敢緩肝貫企岐忌既棋棄軌騎欺犠菊吉喫虐虚峡脅凝斤緊愚偶遇桑刑啓契憩掲携鶏鯨倹賢幻孤弧雇顧娯悟坑孔巧慌拘控甲硬絞綱郊酵克獄墾恨紺魂債催削搾錯撮擦暫施祉諮侍慈軸湿疾赦邪殊寿潤遵徐匠掌昇晶焦衝鐘冗嬢譲錠嘱辱伸審辛炊粋衰遂酔随髄瀬牲請隻惜斥籍摂潜繕措礎粗阻双掃葬遭憎促賊怠滞胎袋逮滝卓択託諾奪胆鍛壇稚畜窒抽鋳駐彫聴超鎮陳墜帝締訂哲塗斗凍痘陶匿篤豚如尿粘婆排陪縛伐伴帆畔藩蛮卑泌碑姫漂苗符赴封伏覆墳紛癖穂募慕簿倣奉崩縫胞芳邦飽乏妨房某膨謀墨没翻魔埋膜又魅婿滅免幽憂誘揚揺擁抑裸濫吏隆了猟糧陵厘励零霊裂廉錬炉廊楼浪漏湾'),
    ('Level Pre-2', '亜尉逸姻韻渦浦疫謁猿凹翁寡禍稼蚊懐拐劾涯垣嚇核殻潟喝括渇褐轄且堪寛患憾棺款缶艦還閑陥頑飢偽宜擬窮糾拒享恭挟矯暁琴菌襟謹吟虞隅靴勲薫慶渓茎蛍傑嫌懸献謙顕弦呉碁侯江洪溝肯衡貢購剛拷酷懇昆佐唆詐宰栽砕斎崎索傘桟嗣肢賜滋璽漆遮蛇爵酌珠儒囚愁臭酬醜充汁渋銃叔淑粛塾俊准循殉庶緒叙償升奨宵尚彰抄渉症硝礁祥粧肖訟詔剰壌浄醸唇娠紳診刃甚迅酢帥睡崇枢据杉畝誓逝斉析拙窃仙栓旋繊薦践遷漸禅塑疎租喪壮捜挿曹槽荘藻霜堕妥惰駄泰濯但棚痴逐秩嫡衷弔懲挑眺勅朕津塚漬坪釣亭偵貞呈廷艇逓邸泥徹撤迭悼搭棟筒謄騰洞督凸屯縄軟尼妊忍寧猫把覇廃培媒賠伯舶漠肌鉢閥煩頒妃扉披罷賓頻瓶扶譜附侮沸憤雰丙併塀幣弊偏遍俸泡褒剖紡僕撲朴堀奔摩磨麻抹繭岬銘妄盲耗戻厄柳愉癒諭唯悠猶裕融庸窯羅酪履痢硫竜虜僚寮涼倫塁累鈴賄枠'),
    ('Level 2', '挨宛闇椅畏萎茨咽淫臼唄餌怨艶旺岡臆俺苛牙崖蓋骸柿顎葛釜鎌瓦韓玩伎畿亀僅巾錦駒串窟熊稽詣隙桁拳鍵舷股虎乞勾喉梗頃痕沙挫塞采阪埼柵拶斬鹿叱嫉腫呪蹴拭尻芯腎須裾凄醒戚脊煎羨腺詮膳曽狙遡爽痩捉袖遜汰唾堆戴誰旦綻酎捗椎潰爪鶴諦溺填貼妬賭藤憧瞳栃頓奈那謎鍋匂虹捻罵剥箸斑氾汎眉膝肘媛阜蔽蔑蜂貌頬睦勃昧枕蜜冥麺餅冶弥湧妖沃嵐藍梨璃侶瞭瑠呂賂弄麓脇丼傲刹哺喩嗅嘲毀彙恣惧慄憬拉摯曖楷鬱璧瘍箋籠緻羞訃諧貪踪辣錮'),
    ('Level Pre-1', '唖娃阿姶逢葵茜穐渥旭葦鯵梓斡姐虻飴絢綾鮎或粟袷庵按鞍杏伊夷惟謂亥郁磯溢鰯允胤蔭吋烏迂卯鵜窺丑碓嘘欝蔚鰻姥厩瓜閏噂云荏叡嬰曳洩瑛盈穎頴榎厭堰奄掩焔燕苑薗鴛於甥襖鴬鴎荻桶牡伽嘉珂禾茄蝦嘩迦霞俄峨臥蛾駕廻恢魁晦芥蟹凱咳碍鎧浬馨蛙蛎鈎劃廓撹赫笠樫橿梶鰍恰鰹叶椛樺鞄兜竃蒲噛鴨茅萱粥苅侃姦柑桓澗潅竿翰莞諌舘巌癌翫贋雁嬉毅稀徽妓祇蟻誼掬鞠吃桔橘砧杵黍仇汲灸笈渠鋸禦亨侠僑兇匡卿喬彊怯蕎饗尭桐粁欣欽禽芹衿倶狗玖矩躯駈喰寓櫛釧屑沓轡窪隈粂栗鍬卦袈祁圭珪慧桂畦繋罫荊頚戟訣倦喧捲牽硯鹸絃諺乎姑狐糊袴胡菰跨鈷伍吾梧檎瑚醐鯉佼倖垢宏巷庚弘昂晃杭浩糠紘肱腔膏砿閤鴻劫壕濠轟麹鵠漉甑忽惚狛此坤昏梱艮些叉嵯瑳裟坐哉犀砦冴堺榊肴鷺朔窄鮭笹匙薩皐鯖捌錆鮫晒撒燦珊纂讃餐仔屍孜斯獅爾痔而蒔汐鴫竺宍雫悉蔀篠偲柴屡蕊縞紗勺杓灼錫惹綬洲繍蒐輯酋什戎夙峻竣舜駿楯淳醇曙渚薯藷恕鋤哨嘗妾娼庄廠捷昌梢樟樵湘菖蒋蕉裳醤鉦鍾鞘丞擾杖穣埴燭蝕晋榛疹秦塵壬訊靭笥諏厨逗翠錐錘瑞嵩趨雛椙菅頗雀摺棲栖脆蹟碩蝉尖撰栴煽穿箭舛賎銑閃糎噌岨曾楚疏蘇鼠叢宋匝惣掻槍漕糟綜聡蒼鎗其揃詑柁舵楕陀騨岱腿苔黛鯛醍鷹啄托琢鐸茸凧蛸只叩辰巽竪辿狸鱈樽坦歎湛箪耽蛋檀弛智蜘馳筑註樗瀦猪苧凋喋寵帖暢牒脹蝶諜銚槌鎚栂掴槻佃柘辻蔦綴鍔椿壷嬬紬吊剃悌挺梯汀碇禎蹄鄭釘鼎擢鏑轍纏甜顛澱兎堵杜菟鍍砥砺塘套宕嶋梼淘涛祷董蕩鐙撞萄鴇涜禿橡椴鳶苫寅酉瀞噸惇敦沌遁呑乍凪薙灘捺楢馴畷楠汝賑廿韮濡禰祢葱撚乃廼之埜嚢膿覗蚤巴播杷琶芭盃牌楳煤狽這蝿秤矧萩柏箔粕曝莫駁函硲肇筈幡畠溌醗筏鳩噺塙蛤隼叛挽磐蕃匪庇斐緋誹樋簸枇毘琵柊稗疋髭彦菱弼畢逼桧紐謬彪瓢豹廟錨鋲蒜蛭鰭彬斌瀕埠斧芙撫葡蕪楓葺蕗淵弗鮒吻扮焚糞頁僻碧瞥箆篇娩鞭鋪圃甫輔戊菩呆峯庖捧朋烹萌蓬鋒鳳鵬鉾吠卜穆釦殆幌哩槙鮪柾鱒亦俣沫迄麿蔓巳箕湊蓑稔粍牟鵡椋姪牝棉緬摸孟蒙儲杢勿尤籾貰悶匁也爺耶靖薮鑓愈佑宥揖柚涌猷祐邑輿傭楊熔耀蓉遥慾淀螺莱洛蘭李裡葎掠劉溜琉亮凌梁稜諒遼淋燐琳鱗麟伶嶺怜玲苓憐漣煉簾聯蓮魯櫓婁牢狼篭聾蝋禄肋倭歪鷲亙亘鰐詫藁蕨椀碗儘兔凰凾厰咒壺峩崕嵳廐廏廚攪檜檮橢濤渕溯漑灌潴皋礦礪龝竈篦纒翆聨苒莵萠葢蘂蕋藪蠣蛛蠅蠏諫讚豎賤迺鉤鎔靱韃韭頸鰺鴈鴦鶯鸚麒麪'),
    ('Level 1', '芦讐屠櫨桝榔弌丐丕丱乂乖舒弍于亟亢亶仍仄仆仂仗仞仭仟价伉佚估佝佗佇佶侈侏侘佻佩佰侑佯侖俔俟俎俘俛俑俚俐俤俥倚倨倔倪倥倅伜俶倡倩倬俾俯們倆偃偕偐偈做偖偬偸傀傚傅傴僉僊僂僖僥僭僣僮僵儁儂儕儔儚儡儺儷儼儻兀兌兢兪冀冉冏冑冓冕冤冢冪冱冽凅凛几凩凭刋刔刎刪刮刳剏剄剋剌剞剔剪剴剳剿剽劈劬劭劼勁勍勗勣勦飭勠匆匈甸匍匐匏匕匚匣匯匱匳卅丗卉卍卮卻厖厥簒叟曼燮叮叨叭叺吁吽听吭吼吮吶吩吝呎咏呵咎呟呱呷呰呻咀呶咄咐咆哇咢咸咥咬哄哈咨咫哂咤哥哦唏唔哽哮哭哢唹啀啣售啜啅啖啗唸唳喙喀喊喟啻啾喘喞啼喃喇喨嗚嗟嗄嗜嗤嗔嘔嗷嘖嗾嗽嘛噎嘴嘶嘸噫噤嘯噬噪嚆嚀嚊嚠嚔嚏嚥嚮嚶囂嚼囁囃囀囈囓囮囹圀囿圄圉嗇圜圦坎圻址坏坩坡坿垓垠垤埃埆埒堊堋堙堝堡塋塒堽塹墅墟壅壑壙壜壟壼夐夥夬夭夲夸夾奕奐奎奚奘奢奠奸妁妝佞妣妲姆姨姜妍姙姚娥娟娑娜娉婀婬婉娵娶婢婪媚媼媾嫋嫂媽嫣嫗嫦嫩嫖嫺嫻嬌嬋嬖嬲嬪嬶嬾孅孀孑孕孚孛孥孩孰孳孵孺宦宸寇寔寐寤寞寥寰尠尨尸尹屁屎屓屏孱屮屶屹岌岑岔岫峙峭峪崟崛崑崔崢崚崙崘嵌嵒嵎嵋嵬嶇嶄嶂嶢嶝嶬嶮嶷嶼巉巍巓巒巫已帚帙帑帛帷幄幃幀幎幗幔幟幢幇幵并幺麼庠廁廂廈廖廝廛廡廨廩廬廱廸彝彜弋弑弖弩弭弸彎弯彗彭彷徂彿徊很徇徙徘徨徭徼忖忻忤忸忱忝忿怡怙怩怎怱怛怕怫怦怏怺恚恁恪恟恊恍恃恤恂恬恫恙悁悍悃悚悄悛悖悒悧悋悸惓悴忰悽惆悵惘慍愕愆惶惷愀惴惺愃惻愍愎慇愾愨愧慊愿愬愴慂慳慷慙慚慫慴慥慟慝慓慵憖憔憚憊憑憫憮懌懊懈懃懆憺懋罹懍懦懣懶懺懴懿懽懼懾戈戉戍戌戔戛戞戡截戮戳扁扎扞扣扛扠扨扼抉找抒抓抖抃抔拗拑抻拏拿拆拈拌拊拇抛挌拮拱挂挈拯拵捐捍捏掖掎掀掫捶掣掏掉掟捫捩掾揩揀揆揣揉揶揄搴搆搓搦搶搗搨搏摧摶摎撕撓撥撩撈撼擒擅撻擘擂擱擠擡抬擣擯攬擲擺攀擽攘攅攤攣攫畋敖敞敝敲斂斃斛斟斫旃旆旁旄旌旒旛旱杲昊昃旻杳昵昶昴昜晏晁晞晤晧晨晟晢晰暈暉暄暘暝曁暹暾曄曚曠昿曦曩曰曷朏朞朦朧霸朮朿朶朸杆杞杠杙杣枉杼杪枌枋枡枅枷柯枴柬枳柩枸柤柞柝柢柮枹柎栞框栩桀栲桎梳栫桙桷桿梟梏梭梔梛梃桴梵梠梺椏椁棊椈棘棍棕椶椒椄棗棣棹棠椚楹楸楫楔楾楮椹椽椰楡楞楝榁槐槁槓榾槎寨槊榻槃榧榑榜榕榴槨樛槿槹槲槧樅榱槭樔樊樒櫁橄橇橙橦橈樸檐檠檄檣檗蘗檻櫃櫂檸檳檬櫟檪櫚櫪欅蘖櫺欒欖欸欷欹歇歃歉歙歔歛歟歿殀殄殃殍殞殤殪殫殯殲殱殷毋毟毬毫毳毯麾氈氓氛汞汕汪沂沍沚沁沛汨沐泄泓沽泗泅泝沮沱沾泛泯泪洟衍洶洫洽洸洵洒洌浣涓浚浹浙涎涕涅淹涵涸淆淬淌淒淅淙淤淪渭湮渙湲渾渣湫渫湍渟湃渺湎渝游溂溘滉溷滓溽滄溲滔滕溏溥滂溟滬滸滾漿滲漱漲滌漾漓滷澆潺潸潯潭澂潘澎潦澳澣澡澹濆澪濬濔濘濛瀉瀋濺瀑瀁瀏濾瀛瀚瀝瀟瀰瀾瀲灑炙炒炯烱炬炸炳炮烟烋烝烙焉烽焜焙煥煕熈煦煢煌煖煬熏燻熄熕熨熬燗熹熾燉燔燎燠燬燧燵燼燹燿爍爛爨爬爰牀牆牋牘牴牾犂犁犇犒犖犢犲狃狆狄狎狒狢狠狡狷倏猗猊猜猖猝猴猯猩猥猾獏獗獪獰獺珈玳玻珀珥珮珞璢琅瑯琥琲琺瑕瑟瑙瑁瑜瑩瑰瑣瑪瑶瑾璋璞瓊瓏瓔瓠瓣瓧瓩瓮瓲瓰瓱瓸瓷甄甃甅甌甎甍甕甓甦畛畚畤畭畸疆疇畴疔疚疝疥疣痂疳痃疵疽疸疼疱痍痊痒痙痣痞痾痿痼瘁痰痺痲痳瘋瘉瘟瘧瘠瘡瘢瘤瘴瘰瘻癇癈癆癜癘癢癨癩癪癧癬癰癲癸皎皖皓皙皚皰皴皸皹皺盂盍盒盞盥盧盪蘯盻眈眇眄眩眥眦眛眷眸睇睚睨睫睛睥睾睹瞎瞋瞑瞠瞞瞰瞿瞼瞽瞻矇矍矚矜矣矮矼砌砒砠硅硼碚碌碣碪磑磋磔碾碼磅磊磬磧磚磽磴礒礑礙礬礫祀祠祗祟祚祓祺禊禝禧禳禹禺秉秕秧秬秣稈稍稠稟禀稷穡穢穹穽窈窕窘窖窩窶竅竄窿邃竇竍竏竕竓站竚竡竢竦竭竰笏笊笆笳笘笙笞笵笨筐筺笄筍笋筌筅筵筥筴筧筰筱筬筮箝箘箍箜箚箒箏筝箙篋篁篌箴篆篝篩簑簔篥簀簇簓篳篷簗簍簣簧簪簟簷簫簽籌籃籔籀籐籟籤籖籥籬籵粃粤粢粨粳粲粱粽糀糅糂糒糜鬻糯糲糴糶糺紆紂紜紕紊絅紮紲紿紵絆絳絖絎絨絮絏絣綉絛綏絽綛綺綮綣綵緇綽綫綢綯綸綟綰緘緝緤緞緲緡縅縊縡縒縟縉縋縢繆繦縻縵縹繃縷縲縺繧繝繖繞繙繚繹繻纃繽辮纈纉纐纓纔纛纜缸罅罌罍罎罕罔罘罟罠罨罩罧羂羆羃羈羇羌羔羝羚羯羲羹羶羸翅翊翕翔翡翦翩翳翹飜耆耄耋耘耙耜耡耨耿聊聆聒聘聚聟聢聳聶聿肄肆肛肓肚肭肬胛胥胙胝胄胚胖胯胱脛脩脣脯腋隋腆脾腓腑胼腱腮腥腴膃膈膊膀膂膠膣腟膩膰膵膾臀臂膺臉臍臑臙臘臚臠臧臻臾舁舂舅舐舫舸舳艀艙艘艝艚艟艤艢艨艪艫艱艸艾芍芒芫芟芻芬苡苣苟苴苳苺莓范苻苹苞茆苜茉苙茵茴茲茱荀茹荐荅茯茫茗茘莅莚莪莟莢茣莎荼荳荵莠莉莨菴菫菎菽萃菘菁菠菲萍萢莽萸葭萼葷蒭蒂葩葆葯萵蒹蒿蒟蓙蓍蒻蓐蓁蓆蓖蒡蔡蓿蓴蔗蔘蔬蔟蔕蔔蓼蕀蕣蕘蕈蕁蕕薀薤薈薑薊薨蕭薔薛薇薜蕷蕾薐藉薺薹藐藕藜藹蘊蘋藾藺蘆蘢蘚蘿虔虧虱蚓蚣蚩蚪蚋蚌蚶蚯蛄蛆蚰蛉蚫蛔蛞蛩蛬蛟蛯蜒蜆蜈蜀蜃蛻蜑蜉蜍蛹蜊蜴蜿蜷蜻蜥蜩蜚蝠蝟蝸蝌蝎蝴蝗蝨蝮蝙蝓蝣螟螂螯蟋螽蟀雖螫蟄螳蟇蟆螻蟯蟠蠍蟾蟶蟷蠎蟒蠑蠖蠕蠢蠡蠱蠹蠧衄衒衙衢衫衾袞衵衽袵衲袂袗袒袙袢袍袤袰袿袱裃裄裔裘裙裹褂裼裴裨裲褄褌褊褓褞褥褪褫襁襄褻褶褸襌褝襠襞襦襤襭襪襯襴襷覃覈覓覘覡覩覦覬覯覲覿觚觜觝觴訖訐訌訛訝訥訶詁詛詒詆詈詼詭詬詢誅誂誄誨誡誑誥誦誚誣諄諍諂諚諳諤諱謔諠諢諷諞諛謌謇謚諡謖謐謗謳鞫謦謫謾謨譁譌譏譎譖譛譚譫譟譬譴讌讎讒讖讙谺豁谿豈豌豕豢豺貂貉貊貎貘貽貲貶賈賁賚賽賺賻贄贅贇贏贍贐齎贓贔贖赧赭赳趁趙跂趾趺跏跚跖跌跛跋跪跫跟跣跼踉跿踝踞踟蹂踵踰踴蹊蹇蹉蹌蹐蹈蹙蹤蹠蹣蹕蹶蹲蹼躁躇躅躄躋躊躓躑躔躙躪躡躬躱躾軈軋軛軼軻軫軾輊輅輒輙輓輜輟輛輌輦輳輻輹轅轂輾轌轆轎轗轜轢轤辜辟辷迚迥迢迪邇迴逅迹逑逕逡逍逞逖逋逧逵迸遏遐遑遒逎遉逾遖遘遨遯遶邂遽邁邀邏邨邯邱邵郢郤扈郛鄂鄒鄙鄲酊酖酣酥酩酳酲醋醂醢醯醪醵醴醺釁釉釐釵鈞釿鈔鈕鈑鉞鉗鉅鉉鉈銕鈿鉋銜銖銓銛鋏銹銷鋩錏鋺錙錚錣錺錵錻鍠鍼鍮鎰鎬鎹鏖鏗鏨鏘鏃鏝鏐鏈鏤鐚鐔鐓鐃鐐鐶鐫鐺鑒鑠鑢鑞鑪鑰鑵鑷鑽鑚鑼鑾钁鑿閂閊閔閘閙閨閧閭閼閻閹閾闊濶闃闍闌闕闔闖闡闥闢阡阨阮阯陂陌陋陜陞陝陟陲陬隍隘隕隗隧隰隴雎雋雉雍襍雜霍雕雹霄霆霈霓霎霑霏霖霙霤霪霰霹霽霾靄靆靂靉靠靤靦靨勒靫鞅靼鞁靺鞆鞋鞏鞐鞜鞨鞦鞣鞳鞴韆韈韋韜齏韲竟韶韵頏頌頤頡頷頽顆顋顫顰顱顴顳颪颯颱颶飄飆飩飫餃餉餒餔餡餞餤餬餮餽餾饂饉饅饐饋饑饒饌饕馗馘馥馭馮駟駛駝駘駑駭駮駱駻駸騁騏騅駢騙騫驂驀驃騾驕驍驟驢驥驤驩驪骭骰骼髀髏髑髢髣髦髯髫髴髱髷髻鬆鬘鬚鬟鬢鬣鬧鬨鬩鬮鬯魄魃魏魍魎魑魘魴鮓鮃鮑鮖鮗鮟鮠鮨鮴鯀鯊鮹鯏鯑鯒鯣鯢鯤鯔鯡鯲鯱鯰鰕鰔鰉鰓鰌鰆鰈鰒鰊鰄鰮鰛鰥鰤鰰鱇鱆鰾鱚鱠鱧鱶鱸鳧鳬鳰鴉鴃鴆鴪鴣鴟鵄鴕鴒鵁鴿鴾鵆鵝鵞鵤鵑鵙鵲鶉鶇鶫鵯鵺鶚鶤鶩鶲鷁鶻鶸鶺鷆鷂鷙鷓鷸鷦鷭鷯鷽鸛鸞鹵鹹麁麈麋麌麕麑麝麩麸麭靡黌黎黏黐黔黜黝黠黥黯黴黶黷黹黻黼黽鼇鼈鼕鼬鼾齔齣齟齠齦齧齬齪齷齲齶龕龠凜熙')
  ]),
  KanjiGroups("JLPT Level", "http://www.tanos.co.uk/jlpt/skills/kanji/", [
    ('Non-JLPT', ''),
    ('JLPT N5', '一右雨円下何火外学間気休金九月見五午後語校行高国今左三山四子時七車十出書女小上食人水生西先千川前大男中長天電土東読南二日入年白八半百父聞母北本毎万名木友来六話'),
    ('JLPT N4', '悪安以意医員飲院運映英駅屋音夏家歌花画会海界開楽漢館帰起急究牛去魚京強教業近銀空兄計建犬研験元言古公口工広考黒作仕使始姉思止死私紙試事字持自室質写社者借主手秋終習週集住重春少場色心新真親図世正青赤切早走送足族多体待貸代台題知地茶着昼注朝町鳥通弟店転田度冬答動同堂道特肉買売発飯病品不風服物文別勉歩方妹味明目問夜野有夕曜洋用理立旅料力'),
    ('JLPT N3', '愛暗位偉易違育因引泳越園演煙遠押横王化加科果過解回皆絵害格確覚掛割活寒完官感慣観関顔願危喜寄幾期機規記疑議客吸求球給居許供共恐局曲勤苦具偶靴君係形景経警迎欠決件権険原現限呼互御誤交候光向好幸更構港降号合刻告込困婚差座最妻才歳済際在罪財昨察殺雑参散産賛残市師指支資歯似次治示耳辞式識失実若取守種酒首受収宿術処初所緒助除勝商招消笑乗常情状職信寝深申神進吹数制性成政晴精声静席昔石積責折説雪絶戦洗船選然全祖組想争相窓草増側息束速続存他太打対退宅達単探断段談値恥置遅調頂直追痛定庭程適点伝徒渡登途都努怒倒投盗当等到逃頭働得突内難任認猫熱念能破馬敗杯背配箱髪抜判反犯晩番否彼悲疲費非飛備美必表貧付夫婦富怖浮負舞部福腹払平閉米変返便捕暮報抱放法訪亡忘忙望末満未民眠務夢娘命迷鳴面戻役約薬優由遊予余与容様葉要陽欲頼落利流留両良類例冷礼列連路労老論和'),
    ('JLPT N2', '圧依囲委移胃衣域印宇羽雲営栄永鋭液延塩汚央奥欧黄億温河荷菓課貨介快改械灰階貝各角革額乾刊巻干患換汗甘管簡缶丸含岸岩希机祈季技喫詰逆久旧巨漁競協叫境挟橋況胸極玉均禁区隅掘訓群軍傾型敬軽芸劇血券県肩賢軒減個固庫戸枯湖雇効厚硬紅耕肯航荒講郊鉱香腰骨根混査砂再採祭細菜材坂咲冊刷札皿算伺刺史枝糸脂詞誌児寺湿捨弱周州拾舟柔祝述準純順署諸召将床承昇焼照省章紹象賞城畳蒸植触伸森臣辛針震勢姓星清税隻籍績跡接設占専泉浅線双層捜掃燥総装像憎臓蔵贈造則測卒孫尊損村帯替袋濯谷担炭短団池築畜竹仲柱虫駐著貯兆庁超沈珍低停底泥滴鉄殿塗党凍塔島湯灯筒導童銅毒届曇鈍軟乳燃悩濃脳農波拝倍泊薄爆麦肌板版般販比皮被鼻匹筆氷秒瓶布府普符膚武封副復幅複沸仏粉兵並片編辺補募包宝豊帽暴棒貿防磨埋枚綿毛門油輸勇郵預幼溶踊浴翌絡乱卵裏陸律略粒了涼療量領緑林輪涙令零齢歴恋練録湾腕'),
    ('JLPT N1', '亜阿哀葵茜握渥旭梓扱絢綾鮎案杏伊威尉惟慰為異維緯遺井亥郁磯壱逸稲芋允姻胤陰隠韻卯丑渦唄浦叡影瑛衛詠疫益悦謁閲宴援沿炎猿縁艶苑鉛於凹往応旺殴翁沖憶乙卸恩穏仮伽価佳嘉嫁寡暇架禍稼箇茄華霞蚊我芽賀雅餓塊壊怪悔懐戒拐魁凱劾慨概涯街該馨垣嚇拡核殻獲穫較郭閣隔岳潟喝括渇滑褐轄且叶樺株鎌茅刈侃冠勘勧喚堪寛幹憾敢棺款歓環監看緩肝艦莞貫還鑑閑陥巌眼頑企伎器基奇嬉岐忌揮旗既棋棄毅汽稀紀貴軌輝飢騎鬼亀偽儀宜戯擬欺犠義誼菊鞠吉橘却脚虐丘及宮弓救朽泣窮級糾拒拠挙虚距亨享凶匡喬峡恭狂狭矯脅興郷鏡響驚仰凝尭暁桐錦斤欣欽琴筋緊芹菌衿襟謹吟句玖駆駒愚虞遇屈熊栗繰桑勲薫郡袈刑啓圭契径恵慶慧憩掲携桂渓系継茎蛍鶏鯨撃激傑潔穴結倹健兼剣圏堅嫌憲懸拳検献絹謙遣顕厳幻弦源玄絃孤己弧故胡虎誇顧鼓伍呉娯悟梧瑚碁護鯉侯倖功后坑孔宏巧康弘恒抗拘控攻昂晃江洪浩溝甲皇稿紘絞綱衡貢購酵鋼項鴻剛拷豪克穀酷獄墾恨懇昆紺魂佐唆嵯沙瑳詐鎖裟債催哉宰彩栽災采砕斎裁載剤冴崎削搾朔策索錯桜笹撮擦皐傘惨桟燦蚕酸暫司嗣士姿志施旨氏祉紫肢至視詩諮賜雌飼侍慈滋爾磁蒔汐鹿軸執漆疾偲芝舎射赦斜煮紗謝遮蛇邪勺尺爵酌釈寂朱殊狩珠趣儒授樹需囚宗就修愁洲秀臭衆襲酬醜充従汁渋獣縦銃叔淑縮粛塾熟俊峻瞬竣舜駿准循旬殉淳潤盾巡遵暑曙渚庶叙序徐恕傷償匠升唱奨宵尚庄彰抄掌捷昌昭晶松梢沼渉焦症硝礁祥称肖菖蕉衝訟証詔詳鐘障丞冗剰壌嬢条浄穣譲醸錠嘱飾殖織辱侵唇娠審慎振晋榛浸秦紳薪診仁刃尋甚尽迅陣須酢垂帥推炊睡粋翠衰遂酔錘随瑞髄崇嵩枢雛据杉澄寸瀬畝是征整牲盛聖製誠誓請逝斉惜斥析碩拙摂窃節舌仙宣扇栓染潜旋繊薦践遷銭銑鮮善漸禅繕塑措疎礎租粗素訴阻僧創倉喪壮奏爽惣挿操曹巣槽綜聡荘葬蒼藻遭霜騒促即俗属賊汰堕妥惰駄耐怠態泰滞胎逮隊黛鯛第鷹滝卓啄択拓沢琢託濁諾只但辰奪脱巽棚丹嘆旦淡端胆誕鍛壇弾暖檀智痴稚致蓄逐秩窒嫡宙忠抽衷鋳猪丁帳弔張彫徴懲挑暢潮眺聴脹腸蝶跳勅朕賃鎮陳津墜椎塚槻漬蔦椿坪紬釣鶴亭偵貞呈堤帝廷悌抵提禎締艇訂逓邸摘敵笛哲徹撤迭典展添吐斗杜奴刀悼搭桃棟痘糖統藤討謄豆踏透陶騰闘憧洞瞳胴峠匿徳督篤独凸寅酉屯惇敦豚奈那凪捺縄楠尼弐虹如尿妊忍寧粘乃之納巴把覇派婆俳廃排肺輩培媒梅賠陪萩伯博拍舶迫漠縛肇鉢伐罰閥鳩隼伴帆搬班畔繁藩範煩頒盤蛮卑妃扉批披斐泌碑秘緋罷肥避尾微眉柊彦姫媛俵彪標漂票評描苗彬浜賓頻敏扶敷腐芙譜賦赴附侮楓蕗伏覆噴墳憤奮紛雰丙併塀幣弊柄陛壁癖碧偏遍弁保舗甫輔穂墓慕簿倣俸奉峰崩朋泡砲縫胞芳萌褒邦飽鳳鵬乏傍剖妨房某冒紡肪膨謀僕墨撲朴牧睦没堀奔翻凡盆摩魔麻槙幕膜柾亦又抹繭麿慢漫魅巳岬密稔脈妙矛霧椋婿盟銘滅免模茂妄孟猛盲網耗黙紋匁也冶耶弥矢厄訳躍靖柳愉癒諭唯佑宥幽悠憂柚湧猶祐裕誘邑雄融誉庸揚揺擁楊窯羊耀蓉謡遥養抑翼羅裸雷酪嵐欄濫藍蘭覧吏履李梨璃痢離率琉硫隆竜慮虜亮僚凌寮猟瞭稜糧諒遼陵倫厘琳臨隣麟瑠塁累伶励嶺怜玲鈴隷霊麗暦劣烈裂廉蓮錬呂炉露廊朗楼浪漏郎禄倭賄惑枠亘侑勁奎崚彗昴晏晨晟暉栞椰毬洸洵滉漱澪燎燿瑶皓眸笙綺綸翔脩茉莉菫詢諄赳迪頌颯黎凜熙')
  ]),
  KanjiGroups("Remembering the Kanji", "http://www.reddit.com/r/LearnJapanese/comments/1a126a/all_2200_kanji_from_heisigs_remembering_the_kanji (RTK1), https://hochanh.github.io/rtk/rtk3-remain/index.html (RTK3)", [
    ('Non-RTK', ''),
    ('RTK1 6th ed.', '一二三四五六七八九十口日月田目古吾冒朋明唱晶品呂昌早旭世胃旦胆亘凹凸旧自白百中千舌升昇丸寸肘専博占上下卓朝嘲只貝唄貞員貼見児元頁頑凡負万句肌旬勺的首乙乱直具真工左右有賄貢項刀刃切召昭則副別丁町可頂子孔了女好如母貫兄呪克小少大多夕汐外名石肖硝砕砂妬削光太器臭嗅妙省厚奇川州順水氷永泉腺原願泳沼沖汎江汰汁沙潮源活消況河泊湖測土吐圧埼垣填圭封涯寺時均火炎煩淡灯畑災灰点照魚漁里黒墨鯉量厘埋同洞胴向尚字守完宣宵安宴寄富貯木林森桂柏枠梢棚杏桐植椅枯朴村相机本札暦案燥未末昧沫味妹朱株若草苦苛寛薄葉模漠墓暮膜苗兆桃眺犬状黙然荻狩猫牛特告先洗介界茶脊合塔王玉宝珠現玩狂旺皇呈全栓理主注柱金銑鉢銅釣針銘鎮道導辻迅造迫逃辺巡車連軌輸喩前煎各格賂略客額夏処条落冗冥軍輝運冠夢坑高享塾熟亭京涼景鯨舎周週士吉壮荘売学覚栄書津牧攻敗枚故敬言警計詮獄訂訃討訓詔詰話詠詩語読調談諾諭式試弐域賊栽載茂戚成城誠威滅減蔑桟銭浅止歩渉頻肯企歴武賦正証政定錠走超赴越是題堤建鍵延誕礎婿衣裁装裏壊哀遠猿初巾布帆幅帽幕幌錦市柿姉肺帯滞刺制製転芸雨雲曇雷霜冬天妖沃橋嬌立泣章競帝諦童瞳鐘商嫡適滴敵匕叱匂頃北背比昆皆楷諧混渇謁褐喝葛旨脂詣壱毎敏梅海乞乾腹複欠吹炊歌軟次茨資姿諮賠培剖音暗韻識鏡境亡盲妄荒望方妨坊芳肪訪放激脱説鋭曽増贈東棟凍妊廷染燃賓歳県栃地池虫蛍蛇虹蝶独蚕風己起妃改記包胞砲泡亀電竜滝豚逐遂家嫁豪腸場湯羊美洋詳鮮達羨差着唯堆椎誰焦礁集准進雑雌準奮奪確午許歓権観羽習翌曜濯曰困固錮国団因姻咽園回壇店庫庭庁床麻磨心忘恣忍認忌志誌芯忠串患思恩応意臆想息憩恵恐惑感憂寡忙悦恒悼悟怖慌悔憎慣愉惰慎憾憶惧憧憬慕添必泌手看摩我義議犠抹拭拉抱搭抄抗批招拓拍打拘捨拐摘挑指持拶括揮推揚提損拾担拠描操接掲掛捗研戒弄械鼻刑型才財材存在乃携及吸扱丈史吏更硬梗又双桑隻護獲奴怒友抜投没股設撃殻支技枝肢茎怪軽叔督寂淑反坂板返販爪妥乳浮淫将奨采採菜受授愛曖払広勾拡鉱弁雄台怠治冶始胎窓去法会至室到致互棄育撤充銃硫流允唆出山拙岩炭岐峠崩密蜜嵐崎崖入込分貧頒公松翁訟谷浴容溶欲裕鉛沿賞党堂常裳掌皮波婆披破被残殉殊殖列裂烈死葬瞬耳取趣最撮恥職聖敢聴懐慢漫買置罰寧濁環還夫扶渓規替賛潜失鉄迭臣姫蔵臓賢腎堅臨覧巨拒力男労募劣功勧努勃励加賀架脇脅協行律復得従徒待往征径彼役徳徹徴懲微街桁衡稿稼程税稚和移秒秋愁私秩秘称利梨穫穂稲香季委秀透誘稽穀菌萎米粉粘粒粧迷粋謎糧菊奥数楼類漆膝様求球救竹笑笠笹箋筋箱筆筒等算答策簿築篭人佐侶但住位仲体悠件仕他伏伝仏休仮伎伯俗信佳依例個健側侍停値倣傲倒偵僧億儀償仙催仁侮使便倍優伐宿傷保褒傑付符府任賃代袋貸化花貨傾何荷俊傍俺久畝囚内丙柄肉腐座挫卒傘匁以似併瓦瓶宮営善膳年夜液塚幣蔽弊喚換融施旋遊旅勿物易賜尿尼尻泥塀履屋握屈掘堀居据裾層局遅漏刷尺尽沢訳択昼戸肩房扇炉戻涙雇顧啓示礼祥祝福祉社視奈尉慰款禁襟宗崇祭察擦由抽油袖宙届笛軸甲押岬挿申伸神捜果菓課裸斤析所祈近折哲逝誓斬暫漸断質斥訴昨詐作雪録剥尋急穏侵浸寝婦掃当彙争浄事唐糖康逮伊君群耐需儒端両満画歯曲曹遭漕槽斗料科図用庸備昔錯借惜措散廿庶遮席度渡奔噴墳憤焼暁半伴畔判拳券巻圏勝藤謄片版之乏芝不否杯矢矯族知智挨矛柔務霧班帰弓引弔弘強弥弱溺沸費第弟巧号朽誇顎汚与写身射謝老考孝教拷者煮著箸署暑諸猪渚賭峡狭挟頬追阜師帥官棺管父釜交効較校足促捉距路露跳躍践踏踪骨滑髄禍渦鍋過阪阿際障隙随陪陽陳防附院陣隊墜降階陛隣隔隠堕陥穴空控突究窒窃窟窪搾窯窮探深丘岳兵浜糸織繕縮繁縦緻線綻締維羅練緒続絵統絞給絡結終級紀紅納紡紛紹経紳約細累索総綿絹繰継緑縁網緊紫縛縄幼後幽幾機畿玄畜蓄弦擁滋慈磁系係孫懸遜却脚卸御服命令零齢冷領鈴勇湧通踊疑擬凝範犯氾厄危宛腕苑怨柳卵留瑠貿印臼毀興酉酒酌酎酵酷酬酪酢酔配酸猶尊豆頭短豊鼓喜樹皿血盆盟盗温蓋監濫鑑藍猛盛塩銀恨根即爵節退限眼良朗浪娘食飯飲飢餓飾餌館餅養飽既概慨平呼坪評刈刹希凶胸離璃殺爽純頓鈍辛辞梓宰壁璧避新薪親幸執摯報叫糾収卑碑陸睦勢熱菱陵亥核刻該骸劾述術寒塞醸譲壌嬢毒素麦青精請情晴清静責績積債漬表俵潔契喫害轄割憲生星醒姓性牲産隆峰蜂縫拝寿鋳籍春椿泰奏実奉俸棒謹僅勤漢嘆難華垂唾睡錘乗剰今含貪吟念捻琴陰予序預野兼嫌鎌謙廉西価要腰票漂標栗慄遷覆煙南楠献門問閲閥間闇簡開閉閣閑聞潤欄闘倉創非俳排悲罪輩扉侯喉候決快偉違緯衛韓干肝刊汗軒岸幹芋宇余除徐叙途斜塗束頼瀬勅疎辣速整剣険検倹重動腫勲働種衝薫病痴痘症瘍痩疾嫉痢痕疲疫痛癖匿匠医匹区枢殴欧抑仰迎登澄発廃僚瞭寮療彫形影杉彩彰彦顔須膨参惨修珍診文対紋蚊斑斉剤済斎粛塁楽薬率渋摂央英映赤赦変跡蛮恋湾黄横把色絶艶肥甘紺某謀媒欺棋旗期碁基甚勘堪貴遺遣潰舞無組粗租狙祖阻査助宜畳並普譜湿顕繊霊業撲僕共供異翼戴洪港暴爆恭選殿井丼囲耕亜悪円角触解再講購構溝論倫輪偏遍編冊柵典氏紙婚低抵底民眠捕哺浦蒲舗補邸郭郡郊部都郵邦那郷響郎廊盾循派脈衆逓段鍛后幻司伺詞飼嗣舟舶航舷般盤搬船艦艇瓜弧孤繭益暇敷来気汽飛沈枕妻凄衰衷面麺革靴覇声眉呉娯誤蒸承函極牙芽邪雅釈番審翻藩毛耗尾宅託為偽畏長張帳脹髪展喪巣単戦禅弾桜獣脳悩厳鎖挙誉猟鳥鳴鶴烏蔦鳩鶏島暖媛援緩属嘱偶遇愚隅逆塑遡岡鋼綱剛缶陶揺謡鬱就蹴懇墾貌免逸晩勉象像馬駒験騎駐駆駅騒駄驚篤罵騰虎虜膚虚戯虞慮劇虐鹿麓薦慶麗熊能態寅演辰辱震振娠唇農濃送関咲鬼醜魂魔魅塊襲嚇朕雰箇錬遵罷屯且藻隷癒璽潟丹丑羞卯巳'),
    ('RTK1 6th ed. (variant)', '剝塡籠頰䇳喻'),
    ('RTK3 3rd ed.', '此柴砦些髭禽檎憐燐麟鱗奄庵掩悛駿峻竣舅鼠鑿艘犀皐畷綴爾鎧凱呑韮籤懺芻雛趨尤厖或兎也尭巴甫疋菫曼云卜喬莫倭侠倦佼俄佃伶仔仇伽僻儲倖僑侃倶侭佑俣傭偲脩倅做冴凋凌凛凧凪夙鳳劉剃厭雁贋厨仄哨咎囁喋嘩噂咳喧叩嘘啄吠吊噛叶吻吃噺噌邑呆喰埴坤壕垢坦埠堰堵嬰姦婢婉娼妓娃姪嬬姥姑姐嬉孕孜宥寓宏牢宋宍屠屁屑屡屍屏嵩崚峨嶺嵌嵯帖幡幟庖廓庇鷹庄廟彊弛粥挽撞扮掠掴捺掻撰揃捌撹摺按播揖托捧撚挺擾撫撒擢捷抉怯惟惚怜惇恰恢悌澪洸滉漱洲洵滲洒沐泪渾涜梁澱洛汝漉瀕濠溌湊淋浩汀鴻潅溢湛淳渥灘汲瀞溜渕沌濾濡淀涅斧爺猾猥狡狸狼狽狗狐狛獅狒莨茉莉苺萩藝薙蓑苔蕩蔓蓮芙蓉蘭芦薯菖蕉蕎蕗茄蔭蓬芥萌葡萄蘇蕃苓菰蒙茅芭苅葱葵葺蕊茸蒔芹苫蒼藁蕪藷薮蒜蕨蔚茜莞蒐菅葦迪辿這迂遁逢遥遼逼迄逗郁鄭隈憑惹悉忽惣愈恕昴晋晟暈暉旱晏晨晒晃曝曙昂昏晦膿腑胱胚肛脆肋腔肱胡楓楊椋榛櫛槌樵梯柑杭柊柚椀栂柾榊樫槙楢橘桧棲栖桔杜杷梶杵杖樽櫓橿杓李棉楯榎樺槍柘梱枇樋橇槃栞椰檀樗槻椙彬桶楕樒毬燿燎炬焚灸燭煽煤煉燦灼烙焔熔烹牽牝牡瑶琳琉瑳琢珊瑚瑞珪玖瑛玲畢畦痒痰疹痔癌痺眸眩雉矩磐碇碧硯砥碗碍碩磯砺碓禦祷祐祇祢禄禎秤黍禿稔稗穣稜稀穆窺窄穿竃竪颯站靖妾衿袷袴襖笙筏簾箪竿箆箔笥箭筑篠纂竺箕笈篇筈簸粕糟糊籾糠糞粟繋綸絨絆緋綜紐紘纏絢繍紬綺綾絃縞綬紗舵聯聡聘耽耶蚤蟹蛋蟄蝿蟻蝋蝦蛸螺蝉蛙蛾蛤蛭蛎罫袈裟截哉詢諄讐諌諒讃訊訣詑誼謬詫諏諺誹謂諜註譬轟輔輻輯豹賎貰賑躓蹄蹟跨跪醤醍醐醇麹釦銚鋤鏑鋸錐鍬鋲錫錨釘鑓鋒鎚鉦錆鍾鋏閃悶閤雫霞翰斡鞍鞭鞘鞄靭鞠顛穎頗頌頚餐饗蝕飴駕騨馳騙馴駁駈驢鰻鯛鰯鱒鮭鮪鮎鯵鱈鯖鮫鰹鰍鰐鮒鮨鰭鴎鵬鸚鵡鵜鷺鷲鴨鳶梟塵麒瞑暝坐朔曳洩彗慧嘉兇兜欝劫歎輿巽歪翠黛鼎鹵鹸虔燕嘗殆孟牌覗彪秦雀隼耀夷嚢暢廻欣毅斯匙匡肇麿叢肴斐卿翫於套叛尖壷叡酋鴬赫臥甥瓢琵琶叉舜畠圃丞亮胤疏膏魁馨牒瞥睾巫敦奎翔皓黎赳已棘聚甦剪躾夥鼾祟粁糎粍噸哩浬吋呎梵陀薩菩唖迦牟珈琲檜轡淵伍什萬邁逞燈裡薗鋪嶋峯巌埜舘龍寵聾慾亙躯嶽國脛勁祀祓躇壽躊饅嘔鼈亨侑梧欽煕而掟籠'),
  ]),
    KanjiGroups("WaniKani", "https://www.wanikani.com/", [
    ('Non-WaniKani', ''),
    ('Level 1', '一七三上下九二人入八力十口大女山川工'),
    ('Level 2', '々丁中丸了五六円出刀千又右四土夕天子小左手才文日月木本正水火犬玉王田白目石立'),
    ('Level 3', '万久今元兄公内冬分切北午半友古台外太少市広引心戸方止母毛父牛生用矢'),
    ('Level 4', '不世主仕他代休先写去号名央字平年打早村気氷申男町百皮皿礼竹糸耳花虫見貝赤足車'),
    ('Level 5', '交会体何作光同回図声売多学弟当形来林毎池社空米羽考肉自色草行西角言谷走近里金雨青音麦龍'),
    ('Level 6', '両亡京全前化南向国地夜妹姉安室州店後思明星曲有東次歩死活海点画直知科羊茶血長食首'),
    ('Level 7', '付以夏失家弱強必教時未末札校欠氏民理由紙組船記辺通週雪風高魚鳥黄黒'),
    ('Level 8', '住助医反合君場対局役所投支数朝森楽決番研究答絵者話買身道間雲電馬'),
    ('Level 9', '乗予事仮使具勝受和始定実客屋度待持新服泳物界発相県美苦表要談負返送部重'),
    ('Level 10', '最業横歌漢病算終線習聞落葉親語読調起路転軽農速進運配酒鉄開院集頭顔飲鳴'),
    ('Level 11', '争令仲伝位低便働共初別利功努労味命好岸意成戦拾指放昔波注洋特神秒競級老育良追'),
    ('Level 12', '倍勉動員商寒島庭息悪悲旅族暑期根植歯泉流消深温港湯球登着短祭章童第都野陽階'),
    ('Level 13', '像億問器士宿情想感整料映暗様標橋殺然熱疑皆福緑練詩課謝賞輪選銀鏡題願養館駅'),
    ('Level 14', '例卒協参周囲固基妥季完希念性技折望材束松格残求的私約能芸術雰頑骨'),
    ('Level 15', '丈仏信列勇区単司坂変夫寺岩帰建式春昨昼晩晴毒法泣浅猫秋築紀英計軍飯'),
    ('Level 16', '係保典冒冗危取品喜園存守専幸府弁急政曜書治浴留真笑箱荷証辞遠門関阪険面'),
    ('Level 17', '側兵原因堂塩官察席常干幻底恋愛敗是果栄梅渉無細結署薬虚覚説識警非鼻'),
    ('Level 18', '借僧句可告喫報座弓忘枚汽洗焼煙祈禁禅種等胸脳訓許試達静類験'),
    ('Level 19', '乱冊加史善団困宇宙容履布徒得忙改昆易暴歴比混減笛節絡続舌若詞財連閥順'),
    ('Level 20', '余個倒厚圧在夢妨妻嫌害尻尾械機災犯率産確穴経罪臭被裕論議防難震飛'),
    ('Level 21', '件任企判制務増委審岡批挙敵断条査検権派済省税素総義解設評認責資際'),
    ('Level 22', '価値副勢各吸営坊域姿宮寝応態提援案状示策統置罰脱藤観誕費賀過領'),
    ('Level 23', '乳俳停備優則割収呼城宅導崎師幹張律施沢準演現看秀職裁規護贅革鬼'),
    ('Level 24', '供型境届展層差庁担株武燃狭環祝管肩腕腰製視触象販質載輸述違量額'),
    ('Level 25', '与候効含居属巻影慣抜捕捜掛景替構模況渡満票絞肥補訟訴豊輩逮限隠響鮮'),
    ('Level 26', '再刺創励占印往従復徴怪我振授接故汗河激独獣突筆菓討豚貯較造郵針鉛障'),
    ('Level 27', '健就屈康怒悩惑招昇暇極段濃症痛眠睡端給締織胃腹訪誘貸迫迷退途郎靴'),
    ('Level 28', '並修傘児冷凍処券博奇妙婦巨幼庫微憲撃攻浜清潔益移程稚精絶綺衆逆録隊麗'),
    ('Level 29', '乾促催僚壊娘宗宴寄怖恐杯板欧江添烈猛略監督積索緊臣航街診詰請閣雄韓'),
    ('Level 30', '乏婚延快懐押撮旗更枕浮渇漏照版盗符系翌背覧詳貧購越遊適預飾騒魅'),
    ('Level 31', '似倉偵嘆均墓孫富尋巣帯幾廊径徳掃探救散既普棒泥粉編脈菜華融豪貨鑑除陸離驚'),
    ('Level 32', '傷党卵厳密序志恩捨採暖机染桜欲永汚液眼祖秘績興衛複訳賛込迎酸銭雑飼'),
    ('Level 33', '否垂宝宣尊忠拡操敬暮漠灰熟異皇盛砂窓筋簡糖納肺著蒸蔵装裏誌諸賃閉'),
    ('Level 34', '丼刻劇勤吐奴射幕承拝推揮損枝歓沿源爪磁粋紅純縦縮聖腐臓芋薦誤豆貴降隷'),
    ('Level 35', '亀互介剣厄噌寿己彫彼恥払杉汁油測湖滞炎為熊獄破紹舎講遅酔酢醤銅鍋'),
    ('Level 36', '伎伸依債及奈姓将幅廃換摘旧核沖津牙献甘療盟継維縄舞般諾貿超踏遺頼鹿'),
    ('Level 37', '償兆刑削募執塁契崩弾恵患戻抗抱抵掲旬昭湾漁爆狙聴臨葬跡跳遣闘陣香'),
    ('Level 38', '伴併傾刊却奏奥妊娠宜慮懸房扱抑択描盤称緒緩繰致託賂賄贈逃避還需齢'),
    ('Level 39', '仙充免勧圏埋埼壁奪岐御慎拒控斐枠棋渋片甲祉稲群謙譲躍邦鈴銃鋼阜隆雇項'),
    ('Level 40', '俊兼剤吹唱堀孝巡戒排携敏敷柱殖殿犠獲繁茂薄衝褒誉透鋭隣雅頻顧駆駐'),
    ('Level 41', '仁伺侵偽儀包墟徹拠拳措撤棄樹潜瀬炭畑至艦虎蛍蜂蜜衣誠遜郷酎鉱'),
    ('Level 42', '克到双哲喪堅床弧括挑掘揚握揺斎暫析枢柄泊滑潟焦範糾紛綱網肝芝荒袋軸'),
    ('Level 43', '刷即垣威封岳慰懇懲摩撲擦斉旨朗柔沈沼泰滅滋潮炉牧珍琴筒籍裂襲誰貢趣距露'),
    ('Level 44', '丘侍俺僕刃匹叫叱吉塔姫娯寸嵐忍斗朱桃梨棚涙砲竜笠粒縁缶翼芽謎辛釣雷髪'),
    ('Level 45', '也井凶卓呪塊塾嫁嬢暦曇湿溝滝澄狂狩疲眺矛硬磨稼翔肌脚舟菌裸賭鐘陰霊頃魂'),
    ('Level 46', '俵吾墨孔寧寮帝幽庄斬架棟椅歳泡涼猿癖盆瞬瞳碁租穂穏綿菊誇鈍錬鍛鍵阻零魔鳩黙'),
    ('Level 47', '伊佐哀唇塀墜如婆尺崖巾帽幣恨憎憩扇扉挿掌柳欺滴炊爽畳瞭砕箸粘粧胴芯虹詐霧'),
    ('Level 48', '咲培塗尽帳彩悔憶斜殴溶灯班畜盾穫耐脅脇蓄蚊蛇貼賢踊輝辱迅遂鉢闇隙霜飢餓騎麻'),
    ('Level 49', '俗刈剛劣勘唯壇奨妃尼征悟抽拓拘桑概浸淡潤煮珠礎紫衰覆誓謀陛陶隔駒鶴'),
    ('Level 50', '亭仰伯偶后唐堤堰墳壮奮峰巧廷彰把搬晶洞涯淀漂漫疫簿翻蟹訂諮軌邪銘駄鬱鰐'),
    ('Level 51', '亮偉召喚塚媛慈挟枯沸浦渦濯燥玄瓶耕聡肪肯脂膚苗蓮襟貞軒軟邸郊郡釈隅隻頂'),
    ('Level 52', '乃倫偏呂唆噴孤怠恒惰慢擁殊没牲猟祥秩糧綾膨芳茨覇貫賠輔遇遭鎖陥陳隼須颯'),
    ('Level 53', '丹准剰啓壌寛帥徐惨戴披据搭曙浄瓜稿緋緯繊胞胡舗艇莉葵蒙虐諒諭錦随駿騰鯉'),
    ('Level 54', '且傲冠勲卸叙呆呈哺尚庶悠愚拐杏栞栽欄疎疾痴粛紋茎茜荘謡践逸酬酷鎌阿顕鯨'),
    ('Level 55', '之伏佳傍凝奉尿弥循悼惜愉憂憾抹旦昌朴栃栓瑛癒粗累脊虜該賓赴遼那郭鎮髄'),
    ('Level 56', '凛凡匠呉嘉宰寂尉庸弊弦恭悦拍搾摂智柴洪猶碑穀窒窮紳縛縫舶蝶轄遥錯陵靖飽'),
    ('Level 57', '乙伐俸凸凹哉喝坪堕峡弔敢旋楓槽款漬烏瑠盲紺羅胎腸膜萌蒼衡賊遍遮酵醸閲鼓'),
    ('Level 58', '享傑凌剖嘱奔媒帆忌慨憤戯扶暁朽椎殻淑漣濁瑞璃硫窃絹肖菅藩譜赦迭酌錠陪鶏'),
    ('Level 59', '亜侮卑叔吟堪姻屯岬峠崇慶憧拙擬曹梓汰沙浪漆甚睦礁禍篤紡胆蔑詠遷酪鋳閑雌'),
    ('Level 60', '倹劾匿升唄囚坑妄婿寡廉慕拷某桟殉泌渓湧漸煩狐畔痢矯罷藍藻蛮謹逝醜'),
    ]),
KanjiGroups("HSK levels", "http://hanzidb.org/character-list/hsk", [
    ('Non-HSK', ''),
    ('HSK 1', '的一是不了在人有我他这个们中来上大和国说时出会你对生能子那下年后作里家多么去学都同现没面起看天分好小些样她本前开想机十工明三关点高很见什二果西月话回老先儿东水名几认系气打女四电少太再做期五书听住北觉师今院识候飞车服怎呢叫影字爱商请视九写八吗吃六医号语七兴星京米客友钱热坐校脑谁哪喜习欢冷汉衣妈读买岁块姐亮朋谢钟雨饭睡喝午店爸桌菜茶狗杯租昨漂椅猫喂苹'),
    ('HSK 2', '为到以要就可也得着过道所然事经动还进但因从日意它长第公已情知正外两间问最手体等新身表给次门常教比员真走条题别报务场件便司眼非白思完色路告边望共让运笑步每快往近夫准始远备百离病息火早找吧考红虽希房黑足孩站诉千男助乐球错晚试送药游室您帮左右穿哥弟慢忙介鱼跑贵班票睛旅笔卖旁阴跳雪肉馆牛纸歌床玩妻休舞姓妹汽课懂绍丈洗唱奶宜累羊零蛋鸡宾颜瓜晴啡篮咖踢泳铅'),
    ('HSK 3', '地而于自发用行种成方法如当定其主理心只实者力把又业重物应向头文相被或己加特信化世位声提解口平更变总数安才结目感接必市直山空决马界放像难且记南求据张该万清带风根干极办议元单调算需花城级复满越容照须包片史乎查轻易除阿李图历突周较注选响参半节护音跟留讲料终答黄奇段故河害双境愿网育船脸刻刚般怕假久拿阳急居环树层句简卡担静检差角皮啊超银怪香铁草脚酒顾换闻坏楚楼画耳短遇康旧春附礼板婚鲜词择健借园牙束练爷嘴戏典盘忘赛趣迎冰努绿街灯夏秋末蓝烧哭冒惯鸟季鼻腿迟辆净冬骑叔爬扫箱舒绩饮朵鞋邮邻聪梯瓶疼熊帽炼搬刷瘦斤胖饿聊碗渴饱甜矮裤衫伞姨刮糕裙衬锻澡啤蕉筷'),
    ('HSK 4', '之部无与民此使性全将由并美利合内度任海通原及论处各入活尔何反受量建计管资命金指克许区保至队社展科基则却光即象式程死交规取拉格术确传观切导争改收言联持济亲林士证失转存台具流连深质价整况亚技际约示究线断精支消增研功广标谈引首局专费尽另仅落随列推众案划律态验责够章志底严例族供效续紧绝察母批按围江纪举父密低止细值仍破倒职速否毛甚普弹苦印预微继惊伤适省卫险排福警获负云停疑洲竟激演判既积富占修降坚免压养怀乱航优著份艺概敢户洋款评座释景登货互付危讨丽序永呼味沙掉杂误减肯败梦散温困封缺恐松虑幸赶剧叶吸呀顺输招脱油材博烟授禁孙篇遍础翻森默熟伙弄刀窗醒购虎扬毕尤竞弃麻申售针抱鼓植页折尊秀染迷诚彩抽浪丰译距符勇厅拜巧戴童乘挂奖厚镜烦签牌咱奋播桥寒聚袋暂估拒忆闹厉穷码偶稍矿抬倍污耐粗悉详允剩漫酸辛餐挺励键扰阅汗骗龄惜仔俩籍凉貌猜怜躺钢寄汤肥尝厌脏幽丢泉祝陪贺琴恼敲暖糖擦肤肚赢址悔邀羽盐傅帅扔傲拾填扮愉慕秒塑羞盒棵谅葡厨鸭谊歉赚萄脾懒骄聘巾堵棒硕戚笨泼郊饼咳桶辣膊趟匙钥胳咸汁垃烤圾逛膏羡暑嗽橡厕袜勺柿乒乓饺'),
    ('HSK 5', '军战政产制代立义神德统形治达强权王设品类领造组英令布未击兵团集华石府似官器称企委曾农装显念青武势古构土投某维革敌致派营巴防施型依群项织斗采杀朝属限威状率独创承股益血素夜初源食待述陆置劳财纳雷模充木龙冲射略范村哈退余痛灵配征挥胜阶沉善执追宣佛控税背阵恶顿守岛托烈索胡靠版宝欧核暗良升临架域括编测屋渐救枪县尚毫移娘智掌遗固席秘均销诗藏损忽巨炮录乡庭妇归含摇补谓毒疗逐寻厂岸炸载避抓荣姑逃顶玉迫洞卷坦宁训私丝握骨访弱鬼软扩盖雄稳亿刺拥齐虚析透替途兄迅套贸唯轮库迹促延震甲伟缓闪哲络纯忍筑贝振圆搞狂措培宽摆伸摩悲拍硬麦操阻订赞纷喊违汇币殊献裁触敬墙召罚享犹彻描妙彼仿闭庆泪朗尾偷虫淡恨繁伴旦潮粮缩挑灰珍幕映隔启泛偿呆衡舍婆灾胆俗辩胸劲辑恢圈摸润堆碰废壁吹糊盾乏诊摄凭抢绪肩幻碎综返薄悄敏碍矛幅颗骂赏贴腰眉恋吓辞尺辈滑绕趋胁插慧媒佩豪兼跃肃驶届欣惠册飘闲频递撞滚贡疯瞧燃锁劝搜勤戒驾柔腐幼践浓竹逻遵饰贷叙沟扶寿询匆奈慰怨躲紫艰慌吐咬挤弯雾屈蛇鼠吨池冠尘浅喷凌赔涂亏寂煤恭湿秩宿烂抖夹昆猪慎玻齿押漠疲醉拳斜档豆涨拼歇桃嘉俊乙妨挣览璃滴姿丑劣匹俱蜂谨糟苗肠挡纲肌膀卧欠夸豫胃睁铃吻脆柴绳眠傻扇柜拦夕姻氛蜜摘披辅盆吵嗯骤漏悠滩嫁催翅锅拆棋唉孕链艳臭趁愁孝冻闯宴矩胶盼脖虹账倡猴寓狮抄晕砍剪叉拐捐歪粘陌窄鞭厘厦恳憾摔愧洒哎钓蝶讽旬撕谦兔荐炭舅裹瞎咨宠兑霉塘帘厢乖娱娶嗓蹲淘嫩壶傍勿踩煮逗炒寞甩燥晒绸屿痒耽魅狡匀熬毯梳蔬捡删浏裔浇姥烫惭蝴梨醋猾皂酱糙屉髦椒桔馒嚏'),
    ('HSK 6', '斯党陈攻苏帝若波异策罪州宗协审皇副抗犯田央伯监露野舰湾吉剑亦恩鲁端探湖予港额督泽灭莫亡圣诺伦奥唐堂宫君谋镇凡诸庄祖暴塔隐蒙欲遭徒姆曲塞侵刑谷川潜抵杰郑混臣雅盛怒残宇猛毁盟丁魔沿啦瓦援夺偏袭侠侧债融纵障讯涉刊爆乌役患仙症倾陷轰撤疾缘杜仪奔珠驻孔翼叹愈罢径恰捕裂泰尖忠炎荒横孤胞魂洪津晓贫仁赖仰艇凶署御奉旋晨伏隆奴丧渡旗甘扎梁皆宙岩荡蒂井壮殖霍撒液番郎忧浮艘伍峰黎贯侦券崇宪慈枝拖墨箭粉泥氏拔愤扑驱掩尸堡储桑惨洁踪勃仇磨拟奏巡剂坡截焦殿伪逼颇昏呈牧牲佳稿腹跌垂脉狱惑陶兽帐昌铺惧盗辉扣嘛董迁凝腾埋涌辖晋狠鉴械赤割揭悟锋祥阔誉筹丛牵鸣旨袖猎臂柱抛牢逊迈欺衰诱狼仗粒遥抚纠钻晶岂峡苍耗菌粹扁循赋抑哀踏恒纽纹渔磁铜跨怖叛遣弥稀捷疫肿削岗晃吞宏癌隶履耀扭坛拨沃绘伐堪牺墓雇廉惩捉覆劫嫌雕闷乳串娃缴唤霸妥搭赴岳舱庞耕锐缝斥宅添挖呵讼氧酷掠祸贪悬唇仓轨枚庙屏寺愚疏颤寸盯辱辨哦腔郁溃忌溜笼丘滋壳痕穴卓贤膜毅锦茫昂皱舌剥窝携陵哼棉饲逆喘罩炉胎蓄竭浑悦诞泡贼亭酬儒泄杆挨吟狭肖霞驳裕顽畜咽勾疆赌畏泊肺缠瞪吊斑涛俘卑葬铭蛮歧廊灌勉盲宰啥胀扯辽抹筒朴咐誓喉妄拘驰栏逝窃纤盈瞬婴颈倘蔽畅赠跪颠遮吁辟瘤嫂框钦庸吼摊嘱衷娇讶耸摧薪淋耻饥崩逢撑翔枯凑溪蠢阐旺碑挪脂谎慨掘逮掏晰罕挽舟骚拓坑兆崖刹芒筋钩棍嚷弦焰耍俯愣饶钉叠惹喻谱煌溶坠滥瓷浴屁漆巢吩啸滞膝茂恕渠辰舶颁袍嘲衔倦涵雀僵肢垄侨舆弊凄捧浸砖蒸陡哑坟眨搏拢昧擅爽搁雌哨巩昔谬谍媳冤鸦蓬巷栽沾诈瞒纺罐壤颂膨谐隙绑嘿挫辐乞哇绣杖衍攀譬肆泣屡躁椎砸帆窜丸斩堤塌贩掀谜捏滨虏卸沼株剖哗劈怯沫竖峻捞鄙魄兜哄颖屑蚁渗秃旱谴稻铸恍贬烛朽佣碌迄绅榜诵禽瞄幢睹贿蔑缚篷淹勘灿敞蜡辜垫妒谣枕丐泌叮掷侮蚀霜蕴妆捆丙钞犬躬昼奠蹈陋侣侄虐堕茎喇绒搅缔嫉灶鸽纬沸畴遏烁嗅叭奢拙栋泻晤稚捣尴诧尬嚼旷芽碳惕汹腥澄萎滔酿诫棕喧伺梢坝敷庇挠搂噪稼寝哺帜揉腻瘫觅僻蔓咋嵌畔涩蹦叨呕凸熄裳凹膛聋沮萌撇苟蚂俭帖煎墅歹伶廓讳瓣枉琢讥呻慷锤桨磅馈溅钙彰眯墟瞻悼拣渺汰镶趴酌浊撼扛峭磕翘熏缀徊肪涕惫挚绎睦窍粥沧怠咙沛崭鞠洽唾柬擎疤钝氓杠诬抒侈徘嗦狈搓赁婪紊兢扒痪宵岔韧憋衅隘濒剔淀缉斟拧蔚眶瀑渣辙潇阱哆辫拽滤睬谤捍瘾磋淆烘赂迸炫嗨惰椭侃瞩蕾炊隧啃舔蹬袱殴侥酝澈锈稠搀筛痹甭唠徙筐曝嘈蔼烹沐掐咀吝肴溉疙揍诽倔攒瘩殃俐拌橙簸惋惮捎唆榨蹋叼秤惦藐馅暧辕馋啬踊暄晾瘸阂挎雹酗拄掰荤饪熨涮锲')
  ]),
  KanjiGroups("Table of General Standard Chinese Characters", "http://hanzidb.org/character-list/general-standard", [
    ('Non-GSCC', ''),
    ('GSCC Level 1', '一乙二十丁厂七卜八人入儿匕几九刁了刀力乃又三干于亏工土士才下寸大丈与万上小口山巾千乞川亿个夕久么勺凡丸及广亡门丫义之尸己已巳弓子卫也女刃飞习叉马乡丰王开井天夫元无云专丐扎艺木五支厅不犬太区历歹友尤匹车巨牙屯戈比互切瓦止少曰日中贝冈内水见午牛手气毛壬升夭长仁什片仆化仇币仍仅斤爪反介父从仑今凶分乏公仓月氏勿欠风丹匀乌勾凤六文亢方火为斗忆计订户认冗讥心尺引丑巴孔队办以允予邓劝双书幻玉刊未末示击打巧正扑卉扒功扔去甘世艾古节本术可丙左厉石右布夯戊龙平灭轧东卡北占凸卢业旧帅归旦目且叶甲申叮电号田由只叭史央兄叽叼叫叩叨另叹冉皿凹囚四生矢失乍禾丘付仗代仙们仪白仔他斥瓜乎丛令用甩印尔乐句匆册卯犯外处冬鸟务包饥主市立冯玄闪兰半汁汇头汉宁穴它讨写让礼训议必讯记永司尼民弗弘出辽奶奴召加皮边孕发圣对台矛纠母幼丝邦式迂刑戎动扛寺吉扣考托老巩圾执扩扫地场扬耳芋共芒亚芝朽朴机权过臣吏再协西压厌戌在百有存而页匠夸夺灰达列死成夹夷轨邪尧划迈毕至此贞师尘尖劣光当早吁吐吓虫曲团吕同吊吃因吸吗吆屿屹岁帆回岂则刚网肉年朱先丢廷舌竹迁乔迄伟传乒乓休伍伏优臼伐延仲件任伤价伦份华仰仿伙伪自伊血向似后行舟全会杀合兆企众爷伞创肌肋朵杂危旬旨旭负匈名各多争色壮冲妆冰庄庆亦刘齐交衣次产决亥充妄闭问闯羊并关米灯州汗污江汛池汝汤忙兴宇守宅字安讲讳军讶许讹论讼农讽设访诀寻那迅尽导异弛孙阵阳收阶阴防奸如妇妃好她妈戏羽观欢买红驮纤驯约级纪驰纫巡寿弄麦玖玛形进戒吞远违韧运扶抚坛技坏抠扰扼拒找批址扯走抄贡汞坝攻赤折抓扳抡扮抢孝坎均抑抛投坟坑抗坊抖护壳志块扭声把报拟却抒劫芙芜苇芽花芹芥芬苍芳严芦芯劳克芭苏杆杠杜材村杖杏杉巫极李杨求甫匣更束吾豆两酉丽医辰励否还尬歼来连轩步卤坚肖旱盯呈时吴助县里呆吱吠呕园旷围呀吨足邮男困吵串员呐听吟吩呛吻吹呜吭吧邑吼囤别吮岖岗帐财针钉牡告我乱利秃秀私每兵估体何佐佑但伸佃作伯伶佣低你住位伴身皂伺佛囱近彻役返余希坐谷妥含邻岔肝肛肚肘肠龟甸免狂犹狈角删条彤卵灸岛刨迎饭饮系言冻状亩况床库庇疗吝应这冷庐序辛弃冶忘闰闲间闷判兑灶灿灼弟汪沐沛汰沥沙汽沃沦汹泛沧没沟沪沈沉沁怀忧忱快完宋宏牢究穷灾良证启评补初社祀识诈诉罕诊词译君灵即层屁尿尾迟局改张忌际陆阿陈阻附坠妓妙妖姊妨妒努忍劲矣鸡纬驱纯纱纲纳驳纵纷纸纹纺驴纽奉玩环武青责现玫表规抹卦坷坯拓拢拔坪拣坦担坤押抽拐拖者拍顶拆拎拥抵拘势抱拄垃拉拦幸拌拧拂拙招坡披拨择抬拇拗其取茉苦昔苛若茂苹苗英苟苑苞范直茁茄茎苔茅枉林枝杯枢柜枚析板松枪枫构杭杰述枕丧或画卧事刺枣雨卖郁矾矿码厕奈奔奇奋态欧殴垄妻轰顷转斩轮软到非叔歧肯齿些卓虎虏肾贤尚旺具味果昆国哎咕昌呵畅明易咙昂迪典固忠呻咒咋咐呼鸣咏呢咄咖岸岩帖罗帜帕岭凯败账贩贬购贮图钓制知迭氛垂牧物乖刮秆和季委秉佳侍岳供使例侠侥版侄侦侣侧凭侨佩货侈依卑的迫质欣征往爬彼径所舍金刹命肴斧爸采觅受乳贪念贫忿肤肺肢肿胀朋股肮肪肥服胁周昏鱼兔狐忽狗狞备饰饱饲变京享庞店夜庙府底疟疙疚剂卒郊庚废净盲放刻育氓闸闹郑券卷单炬炒炊炕炎炉沫浅法泄沽河沾泪沮油泊沿泡注泣泞泻泌泳泥沸沼波泼泽治怔怯怖性怕怜怪怡学宝宗定宠宜审宙官空帘宛实试郎诗肩房诚衬衫视祈话诞诡询该详建肃录隶帚屉居届刷屈弧弥弦承孟陋陌孤陕降函限妹姑姐姓妮始姆迢驾叁参艰线练组绅细驶织驹终驻绊驼绍绎经贯契贰奏春帮玷珍玲珊玻毒型拭挂封持拷拱项垮挎城挟挠政赴赵挡拽哉挺括垢拴拾挑垛指垫挣挤拼挖按挥挪拯某甚荆茸革茬荐巷带草茧茵茶荒茫荡荣荤荧故胡荫荔南药标栈柑枯柄栋相查柏栅柳柱柿栏柠树勃要柬咸威歪研砖厘厚砌砂泵砚砍面耐耍牵鸥残殃轴轻鸦皆韭背战点虐临览竖省削尝昧盹是盼眨哇哄哑显冒映星昨咧昭畏趴胃贵界虹虾蚁思蚂虽品咽骂勋哗咱响哈哆咬咳咪哪哟炭峡罚贱贴贻骨幽钙钝钞钟钢钠钥钦钧钩钮卸缸拜看矩毡氢怎牲选适秒香种秋科重复竿段便俩贷顺修俏保促俄俐侮俭俗俘信皇泉鬼侵禹侯追俊盾待徊衍律很须叙剑逃食盆胚胧胆胜胞胖脉胎勉狭狮独狰狡狱狠贸怨急饵饶蚀饺饼峦弯将奖哀亭亮度迹庭疮疯疫疤咨姿亲音帝施闺闻闽阀阁差养美姜叛送类迷籽娄前首逆兹总炼炸烁炮炫烂剃洼洁洪洒柒浇浊洞测洗活派洽染洛浏济洋洲浑浓津恃恒恢恍恬恤恰恼恨举觉宣宦室宫宪突穿窃客诫冠诬语扁袄祖神祝祠误诱诲说诵垦退既屋昼屏屎费陡逊眉孩陨除险院娃姥姨姻娇姚娜怒架贺盈勇怠癸蚤柔垒绑绒结绕骄绘给绚骆络绝绞骇统耕耘耗耙艳泰秦珠班素匿蚕顽盏匪捞栽捕埂捂振载赶起盐捎捍捏埋捉捆捐损袁捌都哲逝捡挫换挽挚热恐捣壶捅埃挨耻耿耽聂恭莽莱莲莫莉荷获晋恶莹莺真框梆桂桔栖档桐株桥桦栓桃格桩校核样根索哥速逗栗贾酌配翅辱唇夏砸砰砾础破原套逐烈殊殉顾轿较顿毙致柴桌虑监紧党逞晒眠晓哮唠鸭晃哺晌剔晕蚌畔蚣蚊蚪蚓哨哩圃哭哦恩鸯唤唁哼唧啊唉唆罢峭峨峰圆峻贼贿赂赃钱钳钻钾铁铃铅缺氧氨特牺造乘敌秤租积秧秩称秘透笔笑笋债借值倚俺倾倒倘俱倡候赁俯倍倦健臭射躬息倔徒徐殷舰舱般航途拿耸爹舀爱豺豹颁颂翁胰脆脂胸胳脏脐胶脑脓逛狸狼卿逢鸵留鸳皱饿馁凌凄恋桨浆衰衷高郭席准座症病疾斋疹疼疲脊效离紊唐瓷资凉站剖竞部旁旅畜阅羞羔瓶拳粉料益兼烤烘烦烧烛烟烙递涛浙涝浦酒涉消涡浩海涂浴浮涣涤流润涧涕浪浸涨烫涩涌悖悟悄悍悔悯悦害宽家宵宴宾窍窄容宰案请朗诸诺读扇诽袜袖袍被祥课冥谁调冤谅谆谈谊剥恳展剧屑弱陵祟陶陷陪娱娟恕娥娘通能难预桑绢绣验继骏球琐理琉琅捧堵措描域捺掩捷排焉掉捶赦堆推埠掀授捻教掏掐掠掂培接掷控探据掘掺职基聆勘聊娶著菱勒黄菲萌萝菌萎菜萄菊菩萍菠萤营乾萧萨菇械彬梦婪梗梧梢梅检梳梯桶梭救曹副票酝酗厢戚硅硕奢盔爽聋袭盛匾雪辅辆颅虚彪雀堂常眶匙晨睁眯眼悬野啪啦曼晦晚啄啡距趾啃跃略蚯蛀蛇唬累鄂唱患唾唯啤啥啸崖崎崭逻崔帷崩崇崛婴圈铐铛铝铜铭铲银矫甜秸梨犁秽移笨笼笛笙符第敏做袋悠偿偶偎偷您售停偏躯兜假衅徘徙得衔盘舶船舵斜盒鸽敛悉欲彩领脚脖脯豚脸脱象够逸猜猪猎猫凰猖猛祭馅馆凑减毫烹庶麻庵痊痒痕廊康庸鹿盗章竟商族旋望率阎阐着羚盖眷粘粗粒断剪兽焊焕清添鸿淋涯淹渠渐淑淌混淮淆渊淫渔淘淳液淤淡淀深涮涵婆梁渗情惜惭悼惧惕惟惊惦悴惋惨惯寇寅寄寂宿窒窑密谋谍谎谐袱祷祸谓谚谜逮敢尉屠弹隋堕随蛋隅隆隐婚婶婉颇颈绩绪续骑绰绳维绵绷绸综绽绿缀巢琴琳琢琼斑替揍款堪塔搭堰揩越趁趋超揽堤提博揭喜彭揣插揪搜煮援搀裁搁搓搂搅壹握搔揉斯期欺联葫散惹葬募葛董葡敬葱蒋蒂落韩朝辜葵棒棱棋椰植森焚椅椒棵棍椎棉棚棕棺榔椭惠惑逼粟棘酣酥厨厦硬硝确硫雁殖裂雄颊雳暂雅翘辈悲紫凿辉敞棠赏掌晴睐暑最晰量鼎喷喳晶喇遇喊遏晾景畴践跋跌跑跛遗蛙蛛蜓蜒蛤喝鹃喂喘喉喻啼喧嵌幅帽赋赌赎赐赔黑铸铺链销锁锄锅锈锋锌锐甥掰短智氮毯氯鹅剩稍程稀税筐等筑策筛筒筏答筋筝傲傅牌堡集焦傍储皓皖粤奥街惩御循艇舒逾番释禽腊脾腋腔腕鲁猩猬猾猴惫然馈馋装蛮就敦斌痘痢痪痛童竣阔善翔羡普粪尊奠道遂曾焰港滞湖湘渣渤渺湿温渴溃溅滑湃渝湾渡游滋渲溉愤慌惰愕愣惶愧愉慨割寒富寓窜窝窖窗窘遍雇裕裤裙禅禄谢谣谤谦犀属屡强粥疏隔隙隘媒絮嫂媚婿登缅缆缉缎缓缔缕骗编骚缘瑟鹉瑞瑰瑙魂肆摄摸填搏塌鼓摆携搬摇搞塘摊聘斟蒜勤靴靶鹊蓝墓幕蓬蓄蒲蓉蒙蒸献椿禁楚楷榄想槐榆楼概赖酪酬感碍碘碑碎碰碗碌尴雷零雾雹辐辑输督频龄鉴睛睹睦瞄睫睡睬嗜鄙嗦愚暖盟歇暗暇照畸跨跷跳跺跪路跤跟遣蜈蜗蛾蜂蜕嗅嗡嗓署置罪罩蜀幌错锚锡锣锤锥锦键锯锰矮辞稚稠颓愁筹签简筷毁舅鼠催傻像躲魁衙微愈遥腻腰腥腮腹腺鹏腾腿鲍猿颖触解煞雏馍馏酱禀痹廓痴痰廉靖新韵意誊粮数煎塑慈煤煌满漠滇源滤滥滔溪溜漓滚溢溯滨溶溺粱滩慎誉塞寞窥窟寝谨褂裸福谬群殿辟障媳嫉嫌嫁叠缚缝缠缤剿静碧璃赘熬墙墟嘉摧赫截誓境摘摔撇聚慕暮摹蔓蔑蔡蔗蔽蔼熙蔚兢模槛榴榜榨榕歌遭酵酷酿酸碟碱碳磁愿需辖辗雌裳颗瞅墅嗽踊蜻蜡蝇蜘蝉嘛嘀赚锹锻镀舞舔稳熏箕算箩管箫舆僚僧鼻魄魅貌膜膊膀鲜疑孵馒裹敲豪膏遮腐瘩瘟瘦辣彰竭端旗精粹歉弊熄熔煽潇漆漱漂漫滴漾演漏慢慷寨赛寡察蜜寥谭肇褐褪谱隧嫩翠熊凳骡缩慧撵撕撒撩趣趟撑撮撬播擒墩撞撤增撰聪鞋鞍蕉蕊蔬蕴横槽樱橡樟橄敷豌飘醋醇醉磕磊磅碾震霄霉瞒题暴瞎嘻嘶嘲嘹影踢踏踩踪蝶蝴蝠蝎蝌蝗蝙嘿嘱幢墨镇镐镑靠稽稻黎稿稼箱篓箭篇僵躺僻德艘膝膛鲤鲫熟摩褒瘪瘤瘫凛颜毅糊遵憋潜澎潮潭鲨澳潘澈澜澄懂憔懊憎额翩褥谴鹤憨慰劈履豫缭撼擂操擅燕蕾薯薛薇擎薪薄颠翰噩橱橙橘整融瓢醒霍霎辙冀餐嘴踱蹄蹂蟆螃器噪鹦赠默黔镜赞穆篮篡篷篱儒邀衡膨雕鲸磨瘾瘸凝辨辩糙糖糕燃濒澡激懒憾懈窿壁避缰缴戴擦藉鞠藏藐檬檐檀礁磷霜霞瞭瞧瞬瞳瞩瞪曙蹋蹈螺蟋蟀嚎赡穗魏簧簇繁徽爵朦臊鳄癌辫赢糟糠燥懦豁臀臂翼骤藕鞭藤覆瞻蹦嚣镰翻鳍鹰瀑襟璧戳孽警蘑藻攀曝蹲蹭蹬巅簸簿蟹颤靡癣瓣羹鳖爆疆鬓壤馨耀躁蠕嚼嚷巍籍鳞魔糯灌譬蠢霸露霹躏黯髓赣囊镶瓤罐矗'),
    ('GSCC Level 2', '乜兀弋孑孓幺亓韦廿卅仄厄仃仉仂兮刈爻卞闩讣尹毋邗邛艽艿札叵匝丕劢卟叱叻仨仕仟仡仫仞卮氐犰刍邝邙汀讦讧讪讫尻阡尕弁驭匡耒玎玑邢圩圬圭扦圪圳圹扪圮圯芊芍芄芨芑芎芗亘厍夼戍尥乩旯曳岌屺凼囡钇缶氘氖牝伎伛伢佤仵伥伧伉伫囟汆刖夙旮刎犷犸舛凫邬饧汕汔汐汲汜汊忖忏讴讵祁讷聿艮阱阮阪丞妁牟纡纣纥纨抟圻坂坍坞抉芫邯芸芾苈苣芷芮苋芼苌苁芩芪芡芟苄苎苡杌杓杞杈忑孛邴邳矶奁豕忒欤轫迓邶忐卣邺旰呋呒呓呔呖呃吡町虬呗吣吲帏岐岈岘岑岚兕囵囫钊钋钌迕氙氚佞邱攸佚佝佟佗伽彷佘佥孚坌肟邸奂劬狄狁鸠邹饨饩饪饫饬亨庑庋疔疖肓闱闳闵羌炀沣沅沔沤沌沏汩汨沂汾汴汶沆沩泐怃怄忡忤忾怅忻忪怆忭忸诂诃诅诋诌诏诒孜陇陀陂陉妍妩妪妣妊妗妫妞姒妤邵劭刭甬邰纭纰纴纶纾玮玢盂忝匦坩抨坫拈垆抻拊坼坻㧟坨坭抿坳耶苷苯苤茏苫苜苴苒苘茌苻苓茚茆茑茔茕茀苕枥枇杪杳枧杵枨枞枋杷杼矸砀刳奄瓯殁郏轭郅鸢盱昊昙杲昃咂呸昕昀炅咔畀虮咀呷黾呱呤咚咆咛呶呦咝岢岿岬岫帙岣峁刿迥岷剀帔峄沓囹罔钍钎钏钒钕钗邾迮牦竺迤佶佬佰侑侉臾岱侗侃侏侩佻佾侪佼佯侬帛阜侔徂刽郄怂籴瓮戗肼肽肱肫剁迩郇狙狎狍狒咎炙枭饯饴冽冼庖疠疝疡兖妾劾炜炖炝炔泔沭泷泸泱泅泗泠泺泖泫泮沱泯泓泾怙怵怦怛怏怍怩怫怿宕穹宓诓诔诖诘戾诙戽郓衩祆祎祉祇诛诜诟诠诣诤诧诨诩戕孢亟陔妲妯姗帑弩孥驽虱迦迨绀绁绂驷驸绉绌驿骀甾珏珐珂珑玳珀顸珉珈拮垭挝垣挞垤赳贲垌郝垧垓垠茜荚荑贳荜莒茼茴茱莛荞茯荏荇荃荟荀茗荠茭茨垩荥荦荨荩荪茹荬荮柰栉柯柘栊柩枰栌柙枵柚枳柞柝栀柢栎枸柁枷柽剌酊郦甭砗砘砒斫砭砜奎耷虺殂殇殄殆轱轲轳轶轸虿毖觇尜哐眄眍郢眇眊眈禺哂咴曷昴昱昵咦哓哔畎毗呲胄畋畈虼虻盅咣哕剐郧咻囿咿哌哙哚咯咩咤哝哏哞峙罘帧峒峤峋峥贶钚钛钡钣钤钨钫钯氡氟牯郜秕秭竽笈笃俦俨俅俪叟垡俣俚皈俑俟逅徇徉舢俞郗俎郤爰郛瓴胨胪胛胂胙胍胗胝朐胫鸨匍狨狯飑狩狲訇逄昝饷饸饹胤孪娈弈奕庥疬疣疥庠竑彦飒闼闾闿阂羑迸籼酋炳炻炽炯烀炷烃洱洹洧洌浃洇洄洙涎洎洫浍洮洵浒浔洳恸恹恫恺恻恂恪恽宥扃衲衽衿袂祛祜祓祚诮祗祢诰诳鸩昶郡咫弭胥陛陟娅娆姝姣姘姹怼羿炱矜绔骁骅绗绛骈耖挈珥珙顼珩珧珞珲敖恚埔埕埘埙埚挹耆耄埒捋贽垸捃盍荸莆莳莴莪莠莓莜莅荼莩荽莸荻莘莎莞莨鸪莼栲栳郴桓桡桎桢桤梃栝桕桁桧桅桉栩逑逋鬲豇酐逦厝孬砝砹砺砧砷砟砼砥砣剞砻轼轾辂鸫趸龀鸬虔逍眬唛晟眩眙哧哽唔晁晏鸮趵趿畛蚨蚜蚍蚋蚬蚝蚧唢圄唣唏盎唑崂崃罡罟峪觊赅钰钲钴钵钹钺钽钼钿铀铂铄铆铈铉铊铋铌铍铎氩氤氦舐秣秫盉笄笕笊笏笆俸倩偌俳倬倏恁倭倪俾倜隼隽倌倥臬皋郫倨衄颀徕舫釜奚衾胯胱胴胭脍胼朕脒胺鸱玺鸲狷猁狳猃狺逖桀袅饽凇栾挛亳疳疴疸疽痈疱痂痉衮凋颃恣旆旄旃阃阄訚阆恙粑朔郸烨烩烊剡郯烬涑浯涞涟娑涅涠浞涓涔浜浠浣浚悚悭悝悒悌悛宸窈剜诹冢诼袒袢祯诿谀谂谄谇屐屙陬勐奘蚩陲姬娠娌娉娲娩娴娣娓婀畚逡绠骊绡骋绥绦绨骎邕鸶彗耜焘舂琏麸揶埴埯掳掴埸赧埤捭逵埝堋堍掬鸷掖掊掸捩掮悫埭埽掇掼聃菁萁菘堇萘萋菽菖萜萸萑菔菟萏萃菏菹菪菅菀萦菰菡梵梏觋桴桷梓桫棂啬郾匮敕豉鄄酞酚戛硎硭硒硖硗硐硇硌鸸瓠匏厩龚殒殓殍赉雩辄堑眭眦啧晡晤眺眵眸圊喏喵啉勖晗冕啭畦趺啮跄蚶蛄蛎蛆蚰蛊圉蚱蛉蛏蚴啁啕唿啐唼唷啖啵啶啷唳唰啜帻崦帼崮崤崆赇赈赊铑铒铗铙铟铠铡铢铣铤铧铨铩铪铫铬铮铯铰铱铳铵铷氪牾鸹秾逶笺筇笸笪笮笠笥笤笳笾笞偾偃偕偈傀偬偻皑皎鸻徜舸舻舴舷龛翎脬脘脲匐猗猡猞猝斛猕馗馃馄鸾孰庹庾痔痍疵翊旌旎袤阇阈阉阊阋阍阏羟粝粕敝焐烯焓烽焖烷渍渚淇淅淞渎涿淖挲淠涸渑淦淝淬涪淙涫渌淄惬悻悱惝惘悸惆惚惮窕谌谏扈皲谑裆袷裉谒谔谕谖谗谙谛谝逯郿隈粜隍隗婧婊婕娼婢婵胬袈翌恿绫骐绮绯绱骒绲骓绶绺绻绾骖缁琵琶琪瑛琦琥琨靓琰琮琬琛琚辇鼋堞搽揸揠堙趄揖颉塄揿耋揄蛩蛰摒揆掾聒葑葚靰靸葳葺葸萼葆葩葶蒌萱戟葭楮棼椟棹椤棰赍椋椁棣椐鹁覃酤酢酡鹂厥殚殛雯雱辊辋椠辍辎斐睄睑睇睃戢喋嗒喃喱喹晷喈跖跗跞跚跎跏跆蛱蛲蛭蛳蛐蛔蛞蛴蛟蛘喁喟啾嗖喑嗟喽喀喔喙嵘崴遄詈崽嵬嵛嵯嵝嵫幄嵋赕铻铼铿锃锂锆锇锉锏锑锒锔锕掣矬氰毳毽犊犄犋鹄犍嵇黍稃稂筚筵筌傣傈舄牍傥傧遑傩遁徨畲弑颌翕釉鹆舜貂腈腌腓腆腴腑腚腱鱿鲀鲂颍猢猹猥飓觞觚猱颎飧馇馊亵脔裒痣痨痦痞痤痫痧赓竦瓿啻颏鹇阑阒阕粞遒孳焯焙焱鹈湛渫湮湎渭湍湫溲湟溆湔渥湄滁愠惺愦惴愀愎喾寐谟扉裢裎裥祾祺谠幂谡谥谧遐孱弼巽骘媪媛婷巯翚皴婺骛缂缃缄彘缇缈缌缑缒缗飨耢瑚瑁瑜瑗瑕遨骜韫髡塬鄢趔趑摅摁蜇搋搪搐搛搠摈彀毂搦搡蓁戡蓍鄞靳蓐蓦鹋蒽蓓蓖蓊蒯蓟蓑蒿蒺蓠蒟蒡蒹蒴蒗蓥颐楔楠楂楝楫楸椴槌皙榈槎榉楦楣楹椽裘剽甄酮酰酯酩蜃碛碓硼碉碚碇碜鹌辏龃龅訾粲虞睚嗪韪嗷嗉睨睢雎睥嘟嗑嗫嗬嗔嗝戥嗄煦暄遢暌跬跶跸跐跣跹跻蛸蜊蜍蜉蜣畹蛹嗣嗯嗥嗲嗳嗌嗍嗨嗤嗵罨嵊嵩嵴骰锗锛锜锝锞锟锢锨锩锭锱雉氲犏歃稞稗稔筠筢筮筲筱牒煲敫徭愆艄觎毹貊貅貉颔腠腩腼腭腧塍媵詹鲅鲆鲇鲈稣鲋鲐肄鹐飕觥遛馐鹑痱痼痿瘐瘁麂裔歆旒雍阖阗阙羧豢粳猷煳煜煨煅煊煸煺滟溱溘漭滢溥溧溽裟溻溷滗溴滏滦溏滂滓溟愫慑慊鲎骞窦窠窣裱褚裨裾裰禊谩谪媾嫫媲嫒嫔媸缙缜缛辔骝缟缡缢缣骟耥瑶瑭獒觏慝嫠韬髦墁撂摞撄翥踅摭墉墒綦蔫蔷靺靼鞅靿甍蔸蔟蔺戬蕖蔻蓿斡鹕蓼榛榧榻榫榭槔榱槁槟槠榷酽酶酹厮碡碴碣碲磋臧豨殡霆霁辕蜚裴翡龇龈睿䁖睽嘞嘈嘌嘁嘎暧暝踌踉蜞蜥蜮蝈蜴蜱蜩蜷蜿螂蜢嘘鹗嘣嘤嗾嘧罴罱幔嶂幛赙罂骷骶鹘锲锴锶锷锸锵镁镂犒箐箦箧箍箸箬箅箪箔箜箢箓毓僖儆僳僭劁僮魃魆睾艋鄱膈膑鲑鲔鲚鲛鲟獐觫雒夤馑銮塾麽瘌瘊瘘瘙廖韶旖膂阚鄯鲞粿粼粽糁槊鹚熘潢漕滹漯漶潋潴漪漉漳漩澉潍慵搴窨寤綮谮褡褙褓褛褊谯谰谲暨屣鹛嫣嫱嫖嫦嫘嫡鼐翟瞀鹜骠缥缦缧缨骢缪缫耦耧瑾璜璀璎璁璋璇髯髫撷撅赭撸鋆撙撺墀聩觐鞑蕙鞒蕈蕨蕤蕞蕺瞢蕃蕲赜槿樯槭樗樘樊槲醌醅靥魇餍磔磙霈辘龉龊觑瞌瞋瞑嘭噎噶颙暹噘踔踝踟踬踮踯踺踞蝽蝾蝻蝰蝮螋蝓蝣蝼噗嘬颚噍噢噙噜噌噔颛幞幡嶙嶝骺骼骸镊镉镌镍镏镒镓镔稷箴篑篁篌篆牖儋徵磐虢鹞膘滕鲠鲡鲢鲣鲥鲧鲩獗獠觯馓馔麾廛瘛瘼瘢瘠齑羯羰遴糌糍糅熵熠澍澌潸潦潲鋈潼潺憬憧寮窳谳褴褫谵熨屦嬉勰戮蝥缬缮缯骣畿耩耨耪璞靛聱螯髻髭髹擀熹甏擞縠磬颞蕻鞘颟薤薨檠薏薮薜薅樾橛橇樵檎橹樽樨橼墼橐翮醛醐醍醚磲赝飙殪霖霏霓錾辚臻遽氅瞟瞠瞰嚆噤暾蹀踹踵踽蹉蹁螨蟒螈螅螭螠螟噱噬噫噻噼罹圜䦃镖镗镘镚镛镝镞镠氇氆憩穑篝篥篦篪篙盥劓翱魉魈徼歙膳膦鲮鲱鲲鲳鲴鲵鲷鲻獭獬邂鹧廨赟瘰廪瘿瘵瘴癃瘳斓麇麈嬴壅羲糗瞥甑燎燠燔燧濑濉潞澧澹澶濂褰寰窸褶禧嬖犟隰嬗颡缱缲缳璨璩璐螫擤壕觳罄擢薹鞡鞬薷薰藓藁檄檩懋醢翳礅磴鹩龋龌豳壑黻嚏嚅蹑蹒蹊蟥螬螵疃螳蟑嚓羁罽罾嶷黜黝髁髀镡镢镣镦镧镩镪镫罅黏簌篾篼簋鼢黛儡鹪鼾皤魍龠繇貘邈貔臌膻臆臃鲼鲽鳀鳃鳅鳇鳊螽燮鹫襄糜縻膺癍麋懑濡濮濞濠濯蹇謇邃襁檗擘孺隳嬷蟊鹬鍪鏊鳌鬈鬃瞽鞯鞨鞫鞧鞣藜藠藩醪蹙礓燹餮瞿曛颢曜躇蹚鹭蟛蟪蟠蟮鹮黠黟髅髂镬镭镯馥簟簪鼬雠艟鳎鳏鳐癞癔癜癖糨蹩鎏懵彝邋鬏攉攒鞲鞴藿蘧蘅麓醮醯酃霪霭霨黼嚯蹰蹶蹽蹼蹴蹾蹿蠖蠓蟾蠊黢髋髌镲籀籁齁魑艨鳓鳔鳕鳗鳙麒鏖羸瀚瀣瀛襦谶襞骥缵瓒攘蘩蘖醴霰酆矍曦躅鼍黩黥黪镳镴黧纂璺鼯臜鳜鳝鳟獾孀骧鼙醺礴颦曩鳢癫麝夔爝灏禳鐾羼蠡耱懿蘸鹳霾氍饕躐髑镵穰饔鬻鬟趱攫攥颧躜鼹癯麟蠲蠹躞衢鑫灞襻纛鬣攮囔馕戆爨'),
    ('GSCC Level 3', '尢殳邘戋氕仝忉宄讱芏芃邨吒吖钆仳邠犴冱邡闫䜣纩坜芰苊芘芴芤杩轪芈呙岍岜岙伲飏狃闶忮祃诇邲诎诐阽阼纮纻玟邽邿耵苧苾苠㭎枘矻岵岽钐钔钖佴隹郈郐郃肭肸肷饳於怊穸祋卺迳驵驺绋绐砉韨垲埏耇垴拶荖荙荛茈茽荄茺茛荭柃䴓迺砑䶮轵轷轹轺哒耑钘钜钪钬钭矧秬舁俜舣鸧胠胩飐訄饻洚窀袆祏祐祕陧陞绖骃彖恝琊茝莶䓖莙桠桄酎砫砬硁恧翃郪辀辁赀哳晔晖帱赆钷眚笫脩倮虒舭舯瓞鬯鸰脎胲鱽狴狻眢痄疰痃敉浼悃窅窊窎袪袗祧隺陴砮哿翀翂绤骍掭掎聍菝萚菥莿萆菂菍菉厣硙硚硊䴕龁唪翈趼跂蚺崧崞铏铕铖铚铞铥牿稆笱鸺衒舳舲鸼脶脞脟鱾猊觖庳䴔阌羝羕逭袼裈祲谞艴隃绹骕絜堠絷葜葙葴蒇蒈鄚蒉蓇萩蒐葰葎鄑葖蒄鹀楗酦觌硪欹詟辌龂黹睎蛑崾翙赑淼赒铹铽锊锍锎锓颋稌筘筥筅翛舾脿腘腙鲃馉鄗粢遆湓甯裣祼毵矞缊骙䴖遘塥赪搌蒨蓏蔀蓂蒻蓣椹楞榇碃鄠辒龆觜鹍跱蜐蜎赗骱锖锘锳锧锪锫锬稑稙筻筼筶筦傺鹎艉谼腽腨鲉鲊鲌䲟鲏雊飔裛廒瘀瘅鄘鹒鄜麀鄣阘滠裼禋禔禘谫愍戤缞瑷銎墚蔌蓰蔊嘏榍酺酾酲酴碶碥劂䴗夥瞍鹖跽蜾锺锼锽锾锿镃镄镅鹙箨箖僬僦鲒鲕鲖鲗鲙獍飗廑瘗瘥瘕鲝鄫潆漤窬窭禛隩嫜麹劐蕰磉霅踦踣蝘蝤罶镆镈镎镕稹儇䴘艎艏鹟鲦鲪鲬橥觭鹠鹡糇糈翦鹣褯禤遹擐鄹薳鞔黇蕗薢蕹醑觱磡磜鹾蹅螗穄篚篯盦螣縢鲭鲯鲰鲹癀憷懔黉鹨翯髽薿檑醨磹磻瞫瞵蹐镤镥镨矰穙穜穟簕簃簏魋艚谿䲠鲾鲿鳁鳂鳈鳉獯馘襕甓釐鬶鞮藦藨檫黡礞礌蟫镮镱酂馧簠簰鼫鼩臑鳑鳒鹱鹯冁䴙醭蹯蠋鳘鼗鳚鳛麑麖蠃蘘醵颥瀹襫耰鬘趯罍鼱鳠鳡鳣韂糵蘼躔龢鳤籥鼷醾觿蠼')
  ]),
KanjiGroups("Jun Da's Modern Chinese Character Frequency List", "http://hanzidb.org/character-list/by-frequency, https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO", [
    ('Not in Jun Da\'s Modern Chinese Character Frequency List', ''),
    ('Common', '的一是不了在人有我他这个们中来上大为和国地到以说时要就出会可也你对生能而子那得于着下自之年过发后作里用道行所然家种事成方多经么去法学如都同现当没动面起看定天分还进好小部其些主样理心她本前开但因只从想实日军者意无力它与长把机十民第公此已工使情明性知全三又关点正业外将两高间由问很最重并物手应战向头文体政美相见被利什二等产或新己制身果加西斯月话合回特代内信表化老给世位次度门任常先海通教儿原东声提立及比员解水名真论处走义各入几口认条平系气题活尔更别打女变四神总何电数安少报才结反受目太量再感建务做接必场件计管期市直德资命山金指克许统区保至队形社便空决治展马科司五基眼书非则听白却界达光放强即像难且权思王象完设式色路记南品住告类求据程北边死张该交规万取拉格望觉术领共确传师观清今切院让识候带导争运笑飞风步改收根干造言联持组每济车亲极林服快办议往元英士证近失转夫令准布始怎呢存未远叫台单影具罗字爱击流备兵连调深商算质团集百需价花党华城石级整府离况亚请技际约示复病息究线似官火断精满支视消越器容照须九增研写称企八功吗包片史委乎查轻易早曾除农找装广显吧阿李标谈吃图念六引历首医局突专费号尽另周较注语仅考落青随选列武红响虽推势参希古众构房半节土投某案黑维革划敌致陈律足态护七兴派孩验责营星够章音跟志底站严巴例防族供效续施留讲型料终答紧黄绝奇察母京段依批群项故按河米围江织害斗双境客纪采举杀攻父苏密低朝友诉止细愿千值仍男钱破网热助倒育属坐帝限船脸职速刻乐否刚威毛状率甚独球般普怕弹校苦创假久错承印晚兰试股拿脑预谁益阳若哪微尼继送急血惊伤素药适波夜省初喜卫源食险待述陆习置居劳财环排福纳欢雷警获模充负云停木游龙树疑层冷洲冲射略范竟句室异激汉村哈策演简卡罪判担州静退既衣您宗积余痛检差富灵协角占配征修皮挥胜降阶审沉坚善妈刘读啊超免压银买皇养伊怀执副乱抗犯追帮宣佛岁航优怪香著田铁控税左右份穿艺背阵草脚概恶块顿敢守酒岛托央户烈洋哥索胡款靠评版宝座释景顾弟登货互付伯慢欧换闻危忙核暗姐介坏讨丽良序升监临亮露永呼味野架域沙掉括舰鱼杂误湾吉减编楚肯测败屋跑梦散温困剑渐封救贵枪缺楼县尚毫移娘朋画班智亦耳恩短掌恐遗固席松秘谢鲁遇康虑幸均销钟诗藏赶剧票损忽巨炮旧端探湖录叶春乡附吸予礼港雨呀板庭妇归睛饭额含顺输摇招婚脱补谓督毒油疗旅泽材灭逐莫笔亡鲜词圣择寻厂睡博勒烟授诺伦岸奥唐卖俄炸载洛健堂旁宫喝借君禁阴园谋宋避抓荣姑孙逃牙束跳顶玉镇雪午练迫爷篇肉嘴馆遍凡础洞卷坦牛宁纸诸训私庄祖丝翻暴森塔默握戏隐熟骨访弱蒙歌店鬼软典欲萨伙遭盘爸扩盖弄雄稳忘亿刺拥徒姆杨齐赛趣曲刀床迎冰虚玩析窗醒妻透购替塞努休虎扬途侵刑绿兄迅套贸毕唯谷轮库迹尤竞街促延震弃甲伟麻川申缓潜闪售灯针哲络抵朱埃抱鼓植纯夏忍页杰筑折郑贝尊吴秀混臣雅振染盛怒舞圆搞狂措姓残秋培迷诚宽宇猛摆梅毁伸摩盟末乃悲拍丁赵硬麦蒋操耶阻订彩抽赞魔纷沿喊违妹浪汇币丰蓝殊献桌啦瓦莱援译夺汽烧距裁偏符勇触课敬哭懂墙袭召罚侠厅拜巧侧韩冒债曼融惯享戴童犹乘挂奖绍厚纵障讯涉彻刊丈爆乌役描洗玛患妙镜唱烦签仙彼弗症仿倾牌陷鸟轰咱菜闭奋庆撤泪茶疾缘播朗杜奶季丹狗尾仪偷奔珠虫驻孔宜艾桥淡翼恨繁寒伴叹旦愈潮粮缩罢聚径恰挑袋灰捕徐珍幕映裂泰隔启尖忠累炎暂估泛荒偿横拒瑞忆孤鼻闹羊呆厉衡胞零穷舍码赫婆魂灾洪腿胆津俗辩胸晓劲贫仁偶辑邦恢赖圈摸仰润堆碰艇稍迟辆废净凶署壁御奉旋冬矿抬蛋晨伏吹鸡倍糊秦盾杯租骑乏隆诊奴摄丧污渡旗甘耐凭扎抢绪粗肩梁幻菲皆碎宙叔岩荡综爬荷悉蒂返井壮薄悄扫敏碍殖详迪矛霍允幅撒剩凯颗骂赏液番箱贴漫酸郎腰舒眉忧浮辛恋餐吓挺励辞艘键伍峰尺昨黎辈贯侦滑券崇扰宪绕趋慈乔阅汗枝拖墨胁插箭腊粉泥氏彭拔骗凤慧媒佩愤扑龄驱惜豪掩兼跃尸肃帕驶堡届欣惠册储飘桑闲惨洁踪勃宾频仇磨递邪撞拟滚奏巡颜剂绩贡疯坡瞧截燃焦殿伪柳锁逼颇昏劝呈搜勤戒驾漂饮曹朵仔柔俩孟腐幼践籍牧凉牲佳娜浓芳稿竹腹跌逻垂遵脉貌柏狱猜怜惑陶兽帐饰贷昌叙躺钢沟寄扶铺邓寿惧询汤盗肥尝匆辉奈扣廷澳嘛董迁凝慰厌脏腾幽怨鞋丢埋泉涌辖躲晋紫艰魏吾慌祝邮吐狠鉴曰械咬邻赤挤弯椅陪割揭韦悟聪雾锋梯猫祥阔誉筹丛牵鸣沈阁穆屈旨袖猎臂蛇贺柱抛鼠瑟戈牢逊迈欺吨琴衰瓶恼燕仲诱狼池疼卢仗冠粒遥吕玄尘冯抚浅敦纠钻晶岂峡苍喷耗凌敲菌赔涂粹扁亏寂煤熊恭湿循暖糖赋抑秩帽哀宿踏烂袁侯抖夹昆肝擦猪炼恒慎搬纽纹玻渔磁铜齿跨押怖漠疲叛遣兹祭醉拳弥斜档稀捷肤疫肿豆削岗晃吞宏癌肚隶履涨耀扭坛拨沃绘伐堪仆郭牺歼墓雇廉契拼惩捉覆刷劫嫌瓜歇雕闷乳串娃缴唤赢莲霸桃妥瘦搭赴岳嘉舱俊址庞耕锐缝悔邀玲惟斥宅添挖呵讼氧浩羽斤酷掠妖祸侍乙妨贪挣汪尿莉悬唇翰仓轨枚盐览傅帅庙芬屏寺胖璃愚滴疏萧姿颤丑劣柯寸扔盯辱匹俱辨饿蜂哦腔郁溃谨糟葛苗肠忌溜鸿爵鹏鹰笼丘桂滋聊挡纲肌茨壳痕碗穴膀卓贤卧膜毅锦欠哩函茫昂薛皱夸豫胃舌剥傲拾窝睁携陵哼棉晴铃填饲渴吻扮逆脆喘罩卜炉柴愉绳胎蓄眠竭喂傻慕浑奸扇柜悦拦诞饱乾泡贼亭夕爹酬儒姻卵氛泄杆挨僧蜜吟猩遂狭肖甜霞驳裕顽於摘矮秒卿畜咽披辅勾盆疆赌塑畏吵囊嗯泊肺骤缠冈羞瞪吊贾漏斑涛悠鹿俘锡卑葬铭滩嫁催璇翅盒蛮矣潘歧赐鲍锅廊拆灌勉盲宰佐啥胀扯禧辽抹筒棋裤唉朴咐孕誓喉妄拘链驰栏逝窃艳臭纤玑棵趁匠盈翁愁瞬婴孝颈倘浙谅蔽畅赠妮莎尉冻跪闯葡後厨鸭颠遮谊圳吁仑辟瘤嫂陀框谭亨钦庸歉芝吼甫衫摊宴嘱衷娇陕矩浦讶耸裸碧摧薪淋耻胶屠鹅饥盼脖虹翠崩账萍逢赚撑翔倡绵猴枯巫昭怔渊凑溪蠢禅阐旺寓藤匪伞碑挪琼脂谎慨菩萄狮掘抄岭晕逮砍掏狄晰罕挽脾舟痴蔡剪脊弓懒叉拐喃僚捐姊骚拓歪粘柄坑陌窄湘兆崖骄刹鞭芒筋聘钩棍嚷腺弦焰耍俯厘愣厦恳饶钉寡憾摔叠惹喻谱愧煌徽溶坠煞巾滥洒堵瓷咒姨棒郡浴媚稣淮哎屁漆淫巢吩撰啸滞玫硕钓蝶膝姚茂躯吏猿寨恕渠戚辰舶颁惶狐讽笨袍嘲啡泼衔倦涵雀旬僵撕肢垄夷逸茅侨舆窑涅蒲谦杭噢弊勋刮郊凄捧浸砖鼎篮蒸饼亩肾陡爪兔殷贞荐哑炭坟眨搏咳拢舅昧擅爽咖搁禄雌哨巩绢螺裹昔轩谬谍龟媳姜瞎冤鸦蓬巷琳栽沾诈斋瞒彪厄咨纺罐桶壤糕颂膨谐垒咕隙辣绑宠嘿兑霉挫稽辐乞纱裙嘻哇绣杖塘衍轴攀膊譬斌祈踢肆坎轿棚泣屡躁邱凰溢椎砸趟帘帆栖窜丸斩堤塌贩厢掀喀乖谜捏阎滨虏匙芦苹卸沼钥株祷剖熙哗劈怯棠胳桩瑰娱娶沫嗓蹲焚淘嫩韵衬匈钧竖峻豹捞菊鄙魄兜哄颖镑屑蚁壶怡渗秃迦旱哟咸焉谴宛稻铸锻伽詹毙恍贬烛骇芯汁桓坊驴朽靖佣汝碌迄冀荆崔雁绅珊榜诵傍彦醇笛禽勿娟瞄幢寇睹贿踩霆呜拱妃蔑谕缚诡篷淹腕煮倩卒勘馨逗甸贱炒灿敞蜡囚栗辜垫妒魁谣寞蜀甩涯枕丐泳奎泌逾叮黛燥掷藉枢憎鲸弘倚侮藩拂鹤蚀浆芙垃烤晒霜剿蕴圾绸屿氢驼妆捆铅逛淑榴丙痒钞蹄犬躬昼藻蛛褐颊奠募耽蹈陋侣魅岚侄虐堕陛莹荫狡阀绞膏垮茎缅喇绒搅凳梭丫姬诏钮棺耿缔懈嫉灶匀嗣鸽澡凿纬沸畴刃遏烁嗅叭熬瞥骸奢拙栋毯桐砂莽泻坪梳杉晤稚蔬蝇捣顷麽尴镖诧尬硫嚼羡沦沪旷彬芽狸冥碳咧惕暑咯萝汹腥窥俺潭崎麟捡拯厥澄萎哉涡滔暇溯鳞酿茵愕瞅暮衙诫斧兮焕棕佑嘶妓喧蓉删樱伺嗡娥梢坝蚕敷澜杏绥冶庇挠搂倏聂婉噪稼鳍菱盏匿吱寝揽髓秉哺矢啪帜邵嗽挟缸揉腻驯缆晌瘫贮觅朦僻隋蔓咋嵌虔畔琐碟涩胧嘟蹦冢浏裔襟叨诀旭虾簿啤擒枣嘎苑牟呕骆凸熄兀喔裳凹赎屯膛浇灼裘砰棘橡碱聋姥瑜毋娅沮萌俏黯撇粟粪尹苟癫蚂禹廖俭帖煎缕窦簇棱叩呐瑶墅莺烫蛙歹伶葱哮眩坤廓讳啼乍瓣矫跋枉梗厕琢讥釉窟敛轼庐胚呻绰扼懿炯竿慷虞锤栓桨蚊磅孽惭戳禀鄂馈垣溅咚钙礁彰豁眯磷雯墟迂瞻颅琉悼蝴拣渺眷悯汰慑婶斐嘘镶炕宦趴绷窘襄珀嚣拚酌浊毓撼嗜扛峭磕翘槽淌栅颓熏瑛颐忖牡缀徊梨肪涕惫摹踱肘熔挚氯凛绎庶脯迭睦窍粥庵沧怠沁奕咙氨矗盔拇沛榻揣崭鞘鞠垦洽唾橱仕蜘痰袜峙柬蝉蟹谏鹃擎皓朕疤禺铲酶钝氓匣弧峨锥揪杠吭崛诬冉抒庚悍靡晦醋壕锯夭咦侈婢猾徘硝煽皂舵嗦狈靴捂疮郝苛秽茜搓芸酱赁檐饷蕉铀苔赦缎舷筷朔婪紊厮婿寥兢糙卦槐扒裴祀埔絮芭屉痪霄绽宵邑霖岔饵茄韧琪邹瑚憋殆噜忒忿衅淳悖髦孜粤隘濒铮畸剔坞篱淀蓦唬锣汀趾缉嫦斟鞍扳拴诅谟呃懦逞犁忏拧亥佟叱舜绊龚腮邸椒蔚湛狩眶栈薇肮瀑渣褂叽臀妞巍唔疚鲤戎肇笃辙娴阮札懊焘恤疹潇铝涤恃喽砌遁楞阱咎洼炳噬枫拷哆矶苇翩窒侬靶胰芜辫嚎妾幌踉佃葫皖拽滤睬俞匕谤嗤捍孵倪瘾敝匡磋绫淆尧蕊烘璋亢轧赂蝗榆骏诛勺梵炽笠颌闸狒樊镕垢瘟缪菇琦剃迸溺炫惚嗨陨赃羁臻嘀膳赣踌殉桔瞿闽豚掺沌惰喳椭咪霎侃猝窖戮祠瞩菁躇佬肋咄忡雍忱蕾跄硅伎炊钊蝠屎拭谛褪丞卉隧茸钳啃伢闺舔蹬挛眺袱陇殴柿梧惺弛侥琛捅酝薯曳澈锈稠眸咆簧鸥疡渎汲嬉脓骡穗槛拎巳邢廿搀曙樵隅筛谒倭痹猖佯肛奚甭抨蛾唠荧嵩漱酋攘诘篡睿噩怅盎徙鞅漓祟睫攸翎呛筐堑檀寅磊驭惘吠驮瑙炬痉曝恺胺萤敕筝幡霹竺烙毗鸠埠蒜阜嘈乒帷啄鳌毡阙褥搔笋冕狞韶骼蔼烹奄嫖沐噗岑蛟掳咏弩捻圃孚悴诣呱祁捶钠袄澎氮恪雏撮堰彷鹦晖犀腑沽橄掐亵龋嗒咀祺锚匾乓萃贻揖觑吝憔羌诲砾蠕肴撩坍酥袅黝俾嫣穹秧妊溉鹊聿疙蘑睾楷酵茹锌滇辗纂圭幔褒揍诽倔腓颉锄嗔磺攒瘩雳吆悚墩彝囱逍辄桅俨纶悸殃帧俐绮袒籽孰愫拌橙暨敖赘抉淤剌娼顼葵哝酣麓钵琅簸禾铢璧娠彗惋腋螂阪掣劾沥粱嚓惮氖捎羔俟渲榄茧霓鹉胥琶撬橘醫拈笆痊亟渭狙珂刨蜕谚憧瞟馒拗帚钗哧喋箫刁怦缭迥湄磐渝冗闵噶黏蕃弼驿淄饺踞韬婷唆蜒偎榨漉碉皈矜笈枷鲨蹑瀚酪谑癖烬揩炙蜷侏凋漪悻蹋讪搐碘帛诠碾擂苯诃铎戊荀驹攫憬哽踵蟒漾啧吮楠氟怂叼竣偕漩蹭翌臆挝绚崽糜瘢跤阑恬豢汶跷琵憨蜗螅惴戟匮恙抿桢笺蛤瞳藥瓢衹秤跺潦芹哒饬栩曦骷嫡卤丕鬓梓嗖惦浚咔藐荃唧玺汛铐髅渤皿箍馅汾戍痔褶聆涎汞渍奂巅疣傩逵耆蟋鳄讹膺蹿筏釜沂坯峦茬摒蟀撵浒缤嵋珑苞瑾泵钾暧赓叟佚沓撂蛊甥璐晏瘪漳阉蹂鳃琏湃辘僭躏鼾懵镰寐褚攥涧蝙脐辕涣杞煜骥傣嗳祯酉秸捺瑕鑫馋窿楔胱荔蟆湍屹遐轲镯缰桦炖钡羚啬诩绯掖箓涸鸳塾呸抡擞熹坷瓮亘嗟筵跛汕欤壑颍溥姗踊枭暄稷跚涟瀛笙滕踝贰瞰恻嚏迢獗邯睑赡萦珥酮璞羹缄晾俸媲鸾恿蜿犊讷扈蜈翟藕戌蓓鋆谩谀卯谙岐蝎荼镀椰甄蟾蹊泞撸螃檬猓蔷羲瘸蘸蔗傀蚌锢遽邃恚皑锵簌焙昊鹳睽刽鳖噎呗寰唷殡淖诰恣睐婵榈氦靳蛹鸯惬蹙诙眈罡缮胤皋蛀偌疵绛葆黔喙烽儡佼斓嫔颚龈盅娓坂町芥瘠阂挎橇荟啜垛淇瓒篓虱跻龛蹒髯瞠痫掂潼酰镁灸腆筱谆骋壬茗椋蛔潺扉耘槟雹甬谥淞燎蕙蚪蜻郸轶狰楣捋涓荪娄麝蚤薰醮搪谧湮辍瞌梆樟茉岖臼癣穑玷馍呷萼妩伫彤莓岬媛惆鳎啾囔蜓孺徇徵焊岱昵卅飙邙痞隼恫怆桀绶裆盂桧蚓抠嗷槌痘痢芮蚣闩铿飓疱蝌撅蚯斡窠荚耷砚牒赈煦嗫耙榕鞑袤谌醺秆徨橹翡缨锹嵇圪髻嗬辎痣娩谄蛐鹞翱庖籁蓿鳗疟鲇這嚅瘀颔黜黠濑馁洵忐忑砥咂罹糠匝偃淙纫喏闾祛蛰腼涝曜厩疽闰洄煊汐藓璜铬經渥靼酗苓噤咫椿鲫锭罔锺匍祗锰岌馀畹糯胫熠銮沅棣旌豌孢镭驸腌盹熵镐馐嘤癞骰韭阖瞑裨宕戾镌溟牍隽婊鹄埂拄娲虬萱啵蠡芋胭豺啻褛蛆柠掰篆倌咛蛭谡荨莞澹纭潞郅弋飕螳胄蟑猥宓昙锏蟠過柑烯匐濮蟮祐仄偈蜃箴粼嗥褴蕨蓟圩孪杳魇荤诿簪氲摞飒镂舀夙臧蒿貂蜥蹩噼钛钚獾濂铠皙霭鲈叵霾泯碴鸵峪饕瘁睢鬃迩纣夔垠饨榭隍娑篝榔洌浜鲑谔汩浣舐瞭忻咻鹑唑懋皎诒麾辏氐冽箕俚汴宸芍捱摈摺簦箔咝孀怏谝砧馕耄罂漕沣栾榘烷榷俑沱缜鹫蛳剽衢泗臊瘴酚纾晁孛炀叁憩掬椤啮畿掸镣骁椽侗滦荩泓蚱癜酯體癸蚜扪庑歆蝮蹶弈庋喟滂啕蛎獭槁翊龊邺莘燮剁觐铛谗镍臃墒晔燔嘭涿醯箩鄱睨诤坳鹭砷唏伲猬琥殁蚩泾缥殓鳅氰诋刍芷嶙逅舫呓唰茁馑妫骧苷擢峋袂懑蓑與涞祉踹掇沏诳噫饽饪绺谘飧迳铡枞熨鋈荭赊俦戛湎幺凇芪觯龌挞嬴苻嘁鞯肽恸迨钰儆觎讫滓僮媾龇胯涮绾杈赳斛觥疸卞愠拮庠烨龢菠窈罄囤弁奘咣缫腴缈喵潢遛柚郏荻藜琨镳雉橐陽骈蛉艮搽濡寮柩佗啷诜視偻夯闱谖夥枸膑虻筠埽笞臾婀珞粑怵绻殒觊崂颧嗑榛昱蜴鳝噙淼矾硼囿泅邂钜蠹垩乩嗝淦樽诮揆啐淅榉馗辔暹骛鱿苫犷獠詈竦篙诨铰馄蜚峒滢琬靓狻璨犟鸬螨芩嘹锟蜇洹栉俪钍锨瑁壹痿竑粕犄瘙饯抟衲踮龅愎馥梏讣邝艿趺鲟剜绉罅笥衩姣斫鹗腎爻猕晗铩窕仨搡崴酢檄佞孑璀岷舛邕闿铂霁犒馏阈麋麒苁摁涔宥妍铤锷嗲恽麂赝胛哂撷呶噘懔栎桎霰飨揄噔娣薏忝咤嗵迤贲胪鍪泸蔫刈僖咿鹌嗪茏茯岫嵘轱怼铨昕郢咩馊髡澧苣濯盥囡砺佘谶弑楂翦怩蠼霏楹讴锲慵胝砭潍杵樾帼碣诌徕胴钴裟啶铣铱楫赭碛酊魑醛剐畦陂闶阄祚鹘泱趄骅陲郧倜呤燧铉粲骶峁忸渌骞髭戡钨谲苋锃蜊幄闼戕骊虢烩傥妲绌桠袈鎗薮揿杲肓厝莅氤缙衮诟旖硒唁嬗硎裱颦質靥纥煨礴鏖蝈笏羿鼐湟甑炜煲锉笕喑嶂浔弭妪锂苡孳颏醴間渚轭鹬蚝黃膘邛痨褡耦覃虛馔篾兖阋遨爰痂艄耨沤邋焓秣昶種變窣绦俎榫蟪稗謇氩類锴龉烃俣嬷肱鸢笫痤陰菏莆芨阕砣碜鼹長猷竽舸诓錾淬隗悌姘槭邈婕歙稹蹴砒痈镏羯豕鲂蓖匦笤峥徭浃烊補窸酆缢褓蚨翳趔炔誊赜仃勖葺蚴泷蛴結媸俳诖茑逡孱砦跸祜伉溴屐飚蛞鏡掮崆庾橛矸鸨圻缂蒯诹啭饧镉鸪蛩蠖說劭哐崧杼棂螫龃饔遑颢腱襁忾濠牝蛄鲆嗄灏疥苜荞嘣夤砝颞開忤遢旎瘛魉辇見瓤荥涫娌氚臁毂碇毖壅吡缛玮羟還珈颀虼祇佝翕遴珏郛較驗玖蹇逋氅粽诂岢聒髁黍芾淝鲎鞣髋闳潆汨胍阏钤鹜鬈铵戬點崮枰樯脍畲衾蹼題劬咭囫洱刎芏琊碚鳕谪芎恂槿鲢鲧嘧绀郦噱浠潸跏鲶矍苌抻琰鹚龆臬芄呔雒觞钒饫阒槎鸩舂谠阡莒萸妗稔穰蚧餍谯芗菸葩踔厣佻嘌饩钏蠓黩倨腸缬殚钿鎏恁藿囟鄣呋婺绱瓯旃锶酩恹逶缦鸹螟菟阗濉篑醪鲛讦媪邬殇鄯芡嫠肼峤矽讧掼焖愆聩岘靛菖卟姒杷砉袢蚋笳挈關踽黾麼侩凫诔郯韪挲笪鼋莜風菅嵊裢趿箸莴莠阌旯圜涪赍柞嗍囵榧裰笾簟跎巽曷逖骓绔枋镒魃餮讵乜鄢瑭踅馓蟛鳟荛菬忪阍姹纰桉氪氘垅郃汊娉纡缟旮镢傈堋蔺庥枥腭鹕笮髂魍缁槊跞醚吒枳搿鹧蜍舻鏊禳蒺钹蜢鬻珩卮垭苄苕菀骠袷跹瘘騔論磬缶笸鸷頭芰蕲阆纨琮牦砩蠲锒锕郓妯驷鹩舢趸證養芫嗉蠊笊莸饴阃浯枇焱铆擤柢醢呲崾溆潴牖硪碓鹆鬣堀帙雱須進诎獐桁蛱鳏郴幂箝僳疝茴揶呦嗌囹螈脲镊锑胨膈痼鳊赅贽處苤峄桡雎鲋鞫鼬獯昀痍蟊鞴疖熘乇羸嵴栀槲炝炷硐锸鹂裾侪診調珐縯哔屙旆佰僦牯钪掾針仟圮芟崃廪擘笱跗鲅硷苎匏嗾圄彀粳卣勐掴涑浞玳愍畛赧貉擀湫逦椴铄箧刖鲮訇茱啖悭愀朐畈鹨蛘佶缃晟鲱凼苴颛厍匚徉洙氡胗癯鞒锆佤錢飲細勰钺繇螭嵬轸肟肫邨瘿仞奁宄轳熳睇钼蝼跆樗鲰節诶薜铧裥榇馃術蹚怄寤缗硗碡矬鸱虺糅雠帑镧埙啁悒犍硌锩虿蛑艉钅咴筮艏糁鼍肄籴骜砻蜮龀黢劢腫耪鬯畚觳稞鹁鲲稱捌菔獬柘娆篪鲀谰孬伥谇鄄狎闫滟齑遒磔聃綦鲡蔻泠砗钕镫菹胂煅煸螯躅鲠佥罘嶝適坨菽哞徜慊洳渑灞盍钋鸫踯縻萘褫羰腦俅芤隳洮胼罴镛怛芊啉噌嫱绲膻焐裡葎亓倮莼蘅嘞缒镆網伧荏唳檩鸶蚬骱蘖澍韫颎嘏垡腚焯繻怙羧鼙倥亳艽荠昴舨魈醣枵粜甙珲杓楸楦疃蛏蠛髌茔臨诼嬖耒蜣笄跣钣戆蜉喾铍陉薹肷岵瓴荽怫钭窀缯倬摭帔楝痱蚶螬髑紅鼗狷殛裉粝萋葭衽鳢傧喁嫘罟钌裼愦蝽雖锗衿粢醵跫鐾廛墉哌輕扦堇婧暌罱镞蹰陟鳔脘臟岿侔郾唿砹疴麸薨綝滁偾拊撺呒狯猢椁榱罾铳裎鳚眦璎認崞缇蝣萑狲缱晷冼痧統蕖狍憷锛窨袼帏儋绨疠蘩嵝庀汜炅煳泶瓠窳虮蚰邰苊砀捩蹉莪螽覺蘼槔曛蛲鹾隹犸衄觀轉銎泫玢辊瞋墀酐隱堞尥嚯猗逑逯硖噻嵛畀運鲃偬鄞呖溧嬲肭鹈鹱窭黧谵沆嫒塬缣篯酃喱泔溘迕肀秫裣铋蒌曩赀箪朊鳙仫钎芑胙盱糇挹捭悱鬟緩請崤澶甾欹瞽钇鹪鞔缡铯鲚組嘬庹渖湔玎锜锊舾籼阊祕猊燹葑蓼幛岣浼甯瑷敫钔钫锼锿癔穸褊蚍篦麇樘钯禇铒續莩嵯逭遄戗睃鮈瀣皴泮轫褰炱醍锱篁葚難矇驽辚睥鸺筇戥髀驺頸哙濞逄桤攵炻磙疳醭鳇鹮迓眇楮砜謝離約菘馇栌醐唢獍殳仡軟刿葜薅湓搴尕磴锝镅艚殄暝祢豉垴維瓿煺蟥蹀門黼氙铑積線蒡杪肜膂砬硭酽踟鲷蒴藁猡旒硇锍鞲哿皤哏殍漯確織連谂跶橥镬鸲姝茭窆髟畋溏鲔顯喹紹吣羼缧窬骘赉镓邳璩鸸涠溲孥敉筌䜣義衛響蹓垓苒荸甓锪镄脔艟選達眬彘檠胩旄祆伛鲥荦暾脈納缌飏锞趵跖跬僬皲翥祎貢習閉芴菰眙锓訾莳菪槠榍俜觚撄嵫桴晡爨悫锇锖锘蝾糌柙滹睚辦莨尻罨锔筲妣砘谳钽鈤脹遺鄹菡崦狺杌秭舯豇鲵蘧阚悝铌預缑瑗椹旰魆蓍蕹岜钐锬镪绡檎穀茕話縮顧荈侉渫辂欷轾麴戢趼誤芈苈缍歃燠耜顸蚵哓澌郜徼籀陬蕤叻猞洇锎舳缋镗褙耋聬鳡鲌鰽筆簡計語謂袴巯吖猁桷砼锾颟跽悛桕艨颡髹桫鬆練總膽貝葸屣獒瘌佴锫隰醌萬矯鰕岽昃螓垧廨骺黥豳議絡護釋隨荑莶蓊揎娈嫜毽砑碶剀薷怃怿骐腧霈蝻鵰讀墼坩甏鹇鹣舴鲭傺枘秕糨忉磲顒蟲訓侑萁葳呙鹋貘葶枨棹纛籤規資嶷妁杩鹛羝骖祧給淠畎箨鳐識遠谿剡吲嫫戽糗鸮蕰坼璺栊镝疔瘰谮辋碥豂竅讓黒劂潋孓螋鲳铙塄萆碲粋纻沭祏電鱲頻設試項鄩鱖鱧怍糍鸻仵柰棼氇氆烀镔珉鞬範膠眾鶇囝犴镠觇钆蚺蝓趑貔躞氽绂栲鹎襻蓚貪祓繼脫郿骝檫砟蝰猱缵沔彖黻眢車陳雜驚龍鮠茛蕈骀樨昝餂镎酡鳜觋礅垆坻荇扃磻郗阇腈铈臥顱級階顟衖珙襞劁隈胬纮翙茀荜溱酤腳記許錯鱇圯柽瞀铖粞撙铊圹菝迴岙漶缏貊粫徂洎礌膿葉險雙餘邠邽溽棰舭艋靜聱尢藚佾蕻狁绁牾慝蜱鬘膚虧邊髮埚堙菥萏玟椟铗颙踬筚矻搠圉浍閱蛸礎討鎮鮊芘萜鄗惝毵鲽酞絕哚溷缞踰搦帻铦鲴髫盡蓋製載週陸醡儇狴迮鍬趱椠赟陔坌悃塍疬麈絜脩赒埒镡镨骎骙薑鼩雰穩藴責鮮鳑豨琚觫鲦刳拶掊泐瘗雩麿檗鼂詳際褔铟聽觸靈鲏蒗魟遹攴蝥茆蓁嚆忮篌菧卺郫篠複該貴辯飛犰狳陠蹁蓐稜菃埝蕞喈戋赙磉郤聍铷硏腘興雞鬱鳴麥鮟鳈秾邗釐矧舁貅瞇骢阼垸墁攮柝梃眚箜簏綮鲩諡茇摅顐蜾龂䦟臍膩諸讉鎯脒箬鲻埸颃蒹瞍铫蒐蹻幞阯觏媵钬襦簋翮蹯艖貓鐮負順鲿緊蹠攉禊箐镟癍霪袪劓殂脞霨饾耵泺埤碁鲐鷟膬茲粯糞聲貼陴橼驩唣蜩埯蓥袝谞馘谫輶廑瘐躐黟纔礙膯華藭禆號談費顏飯稓縠揠绐鸰搛黹恧粎柒裒栳钸饸譞販铕絷蒨蓣迻釆鲕頗鍏鷉郄埘薤鲞鼯坭蔌缳靦筸蘋夼椐轹脬眍饹瘥瘵蝦誌邴鉁鞮舄麄翛覩纩蓮唛袓祂轎紀纖輔鉀領螵鸊鮡禛袆謴邾鮣酲龁汔眄眊鬲阨靸臉贇酺狃轺霅鬂鼷蠃埴鴥隊髆綱膮謹铪鹼簳終綜裝訉銀鲉蕿袊汆硃仝趽堍揸忭銧妤頫緡讟龠垤擐噍洫滏璁癃邡絁鍩趨蒽絲膫臅茖蘇詞詾贆蹨農錄鐘鰜鹽赕鯔鯮蔯貙餬躜鳀鹡䴘蠋钲蜁兕阽鎰绋铓爝磾葷螘仂雲顗蟫蕺骃蔀诪猹鋬盤齾埕聞舉虡評鍋陣紬訢蔎繸绖埭駮鰡鵳柁筴珧贳贶腩臌礓袛貐蹐圬堠屦驵鑑桄霑憝瘳騃茌辀胠埏腠靰鞡缻輳闆铼紤翹聯詢課豐賴輸遲鐣齡莤鱯缽邲唼鐻閟駚篥茈肏萩跐蹅瞢罽聭辻铚箦踣菑蹟捃瘕睺閒鈦顩鳓闇鹹䥇禍窩純縱聖聛脮衝訊馬諹誖蕅鰨睒笰籥翧镩耧蜞舡鰲鹀䴙罣觍絽羶臜薙觔躼岈潲枧觌膦礞蝤螗酹醅絅纁葰郇躄茼洧滠澉鎭铏閤赆赇顣骕飑訄輓鉤鋹钘陁耱繫鋵鱵黨禿貧買賈榀緣膶茐螝訙誘賦贅鄬釤鍵閮隻飽齒鯆逿鮀鯝鰁鱤郕镴韻鮄鲙鳁齁舖膹袣謿陧坜坫甍绠恝飗镙镱騾魋硱祫筍箖袧迯郙酖遘阘眭餗耖鯒邶絼颥篚鳘䥺虒裈遆麑粚託鄚軌饋銳粌紙職臏莖葌豬貏違鄉闅闊頂飢驅魚鳉鴱鶎黴祼鬛镈瞓罶羑黉霚笹郐溻骯礡袉訚谉莛哕滗瀹鏰稃眰眳矞硚禋翀苾襕趥茺軿逌唪庳殪隃糈鲄龜碕鲣綎栝轵雔頠穈翃膭衒盇礦譢鳰遞鴫笟莾蒼蟬袑訒講讝購趕鈧鈩閃閷頉髤龤薿鱥觝鮻鳤穉觱轘鐓筘鲝睏蔸镚痦秵臎葴蝟訂泖骟锽犋眵耩筢躔鬏黪䞍祔箠舲蒷蜺襢謺劐貯搋醊廒洚胲韥饘馂筅鳆鲊麗篸腄臑诐仳趩篩簾絪绹膵蕗蝘袠賸葙遊饑驀祪禘臺菍髒軸釘頃仉氕矔緒脅臒苿菢蔂藞袩貞賣跍跓蹤軍邿鄰醿鈨鋼駵駸鰪鱾䝼賨艞鹟钁鞓鰉監穊蕡鑨楱靹鷃鼱眫艆褯剞蔟靿飭瘼酴鼢睆硁秬穪筦粡粣綖裏刭跼蒇挢邆彡猃闉阓阛靺鞨铥瘅駰騻箅箢觖麆齮糀虯瘊絛聴蘭讬揲镮钷睪砲稅翫荅菉袚褋贠跡踦遯鉅鎌靉韲餖鶺麕瞼菵蟭錏踐輾銷閣頁驟碼禎禦稖稟竇笇篂緛編縿舊蓴蕚蘆蝿袃親訴讕讚財贏軅軓釙鉄錆閶鯕鶕麨䜩䴗脭鲯鐏魾眎睞窋籠綠縡縫肅鉏謦麹蔔繐眥粺缊艈蓇蛣蹾掎哜鄦陞韰飖镲麃禑筰聠茷螀袞褧賮赗踡揞遝酂酇醜檑雮氍腙飩痖髣髳酎鲒鲪鹯麜齸齻粩詣隄簰蒾蓏薳藛蚢蓠蓰遡郋鄜錞靣鸂麐麚齧䌷睊砢碻絃茝菴袥襍覗詩諥跂辵邅醨頍疰觜鴿笭糷纘翉胵芖蔣蔦蛚蛯蜏讞賲钃餈馧麤鼶禱臓鈍錫紛遙螣铽竝粊紗紮絺絿緯脦臇臋葍葞葯葻藙蜔螕蟻襲觼觿詼諝貨賀趧跉躍軒輪邉鄶酁釀鈾鈿鍊闀闄腽霧韌頎額顫顬髿鴣鶝鷣齋鋊隤艦譟蒉磜綼輋頨閗鮍鯡鲹禣粏綿臐迏鋾鐇铻鮼鼈込篰痄睄磡窔筊羺腪臢荄蓡蝀詥豀苠郞骒戤铞耢麯秱筼綈翬脧茣菒蓯蕝詝謱冁踧茚辌辒郪鄘鄠帱鈇缲雚雟韺頵顝镘鬋酾鳣鴦麀麉麊麣藬鏘鞚飔鴃齏礄誥醲毳築絫脺苧蚘蝺蠶裀詧貍踘蹷蟓盦瞆矰磥祮稛箾翂胊蓺薾襱覅讏跅踆蹔軐轪鄤醰鑟铔閛陙霳顑镤鵲竚紩聦餅鶄競簷糵紖訪豎趦隸禠籓镥盜矝笖笧簢簻籌粍綍縕罋罷翜膰膲菂葦薢藷螞蠻袀袐覍訌訛詿諄譜豈賢賹遷釛鈣鈱鈶鍛鍦鐵閯閺閻隂頌頰顆顪飼駕駝驌驘鰠鰹鲗鶒鶗鷥鷹齊硙禜糢藠镦蕂霮沩颼禬鴪鮨鱣盝眹睖磫禫繨薦褱鏏鮁鹓繟繺沲餦篤踺祦篲糰絙纄脝茊菫蓞酦醾锳钶鲼齄鴨鷧㧟祋箯粐粦粭紃脰芃苽莿菆藗藧袵裯褵襆詤譓跊軈苘迺掭邇邘鄳猸艴鑕柃闒毹脶颋鵀鶜鶟鷱鷲鹍麖䦆軎稂蒞蠆褲佧紵緌蠾裲郈鋐餱瓞驙鯙眆睠瞫矅碃禃秔穻箇籐絏纕翐耈耎脷膕艐艷苙葹蓂蔲薋蛷蜑衂衋袿訕訝詠誳諆讱軃轝郀郵鉐鍧鍼鏦镵閭闢陗陼韈骫骳骹髠髥鳒鶡龒籂翯莚萗転鄷靭馉騙驊鼰綑績臘臛賜贈蹣軡鋸錐顎瞐銶钖矊矘矚矡硽磿礈礜秲窮竄笗箘箽簍簜粷絨絹緷緻繉繙罁羅羇聣聰脙脛脻脼腗艜萊葘葢蔥藍藘藝蘿蛬螁螚螤袇袌袔袦袨覂訃訋詫詬詮詻誠謬譃譄譯譽賰趮蹱軙軠輩辭遜鄧鄫鄿酀釡釢鉃鍍鍎鎖闃鞗韱頹願顳餁餃餵馮馳駛騎騺鯚鰟鱉鳛鴟鴮鴲鴷鷷鸀麎麡麧鼇鼞鼤齺齽龑裏䦶䲡砮綟緜繑纑罈蠙輴酨鏂駹鎪瞕窪肻蠔鐰綵鮰鳾虰驎荬鑛犏鞧鮋鰷鶲盕盩盻眖砛硈禢禥窼竏筈筽篴籆籇紏肣胑臮苲蒃虗蜌跘鞦驄鷭鸼鹐矄魖鴐薀謏脎締聧脜艤荖蕌蠷褏觽踫蹽軉軛墚搌擗哳鋻楗韂飆饏耥髼篼鬑醑鴧眜瞷磦礨祃祲祻窊簥籲縢繌繒聜胔胾脨膼艕苼莻蓨蓵蓾藦虀蚈蛡蛻蝝蝹蟿衼褦襶覐詯誴諓謧謪譁貤赪踖軆輈鄛鄡醖屺鍑鏉雊顓飐稆駳騽骍筻魱舣鮾鯋鯏鶃鶫齛矙絾袗襬漤闕鬐鲾鴾稭籄聺褹訟鏕齆盫矎礋窌簼糴纴罵翚耰艧藇虖蚖蜎蜨蠭詟詵譔豭趙趬阢圊醃録鍮鍸闚阤霫鞎韗鬖鳠鴼鷇黇黡齣盞眅磈磳穫窅窾筭箣簃簺粴糦絟緺縩罍翣聟肊肙肞臞苶菭葖蕳蚒蜪蝕蠜袕裋裩褌褎襫覈觭訆訏訽詨譻诇貑跱坶躘輖轇轋轕迒郘醄醼鋋鏁鏭鐄鑣鑷辁阸牿鞝頞瞵饤駃駉騠驡髪鬚鬿鮌鯁鱻鶚鷫鹖磩磭稌穃綂膥膱臿艎苃茍蒟藣虈蜐訅詭讈貿趷蹌蹹鈰銑鋫鍔鐨餉騛鯛鰤鳳鵂鶢鶳黋齢磚緲繳聝膴芵藫覓誕誡貎賄跰踥迆逕逤鏢鏤鑄鑽頷鴉鴰麅礱祿缷虙齗裓铹睙矟硣磹礀禮秶窇竷笣篃簬簯粓粶紋紓絞緹縷縼繆繕繚繞绤罆羈翆翑聵脵臄茽莊莢莵菕蓛蓷蓸蔘蔞蕘蕼薔藖藢藶蛢蟯蠄蠈蠎蠣襪覙訑訣詰詸誰諏諛諮諱謥謨譫貋貛貫賓賞贁贂贉趤趯趶跔踴蹆塥輝輰輿轂邁邼釟釠釣鈉鈴鈺鉂銊銘鋤鋭錃錈漭錨鍤鏆鐖鐧鐳鑱鑾镃閬閾閿陜陝霠鞏鞖韨韼韽頒頤顛飳飸餆館饅駐駡駷騁騫騷騼髕魜鰫鱗鱽鲬鴻鶆鶊鷳鷿鸁麞鼏鼜鼫齦䦂䲟䴓䴕䶮盬祅禡禭糱縂蠥軷鄮釱銦錣鑢钑饟鯅鼊䴖簫粛粻饈盌瞂鋅靮盨県箥簕臖鎔鏐顔盿萵蔊覥貲驢鶸磑窎詒鉔鏱隺饜荘蒻蔴裛鈙鎋鑀髴鴓鸴黿秹茢蘁蚑鏻霤霩頺餚鯂籔蕁蘘雑鬶鯵鰧鱂鳂鵟盠盳盽眃眏睧硄碔碦碸磃礘礮祘禤秌秙秢稧稬稲稸穜竒筶篬籒籜籞籶糂糉綡綶緄緗緼縁縋縞繤繧繬纃纉纒纗罯羀耴肍腨膗膟舦艊菄葾蒕蒘蒧蓃蓆蔱蘔蟨蠪襖誇謟讙谽踨躉躱輗釔鋕鎚韆鯶鳋鹒篭縜腣赲馻磞睕瞜碠磽簘腃腵蓳覇醱銝巛鐴鑵隩颺飮飰餇饐痃駞鴜㳠䁖睅睍碭碽磸礉礽祾禌筥簴紣絍縆繀繃羕羵耇聫脗臯艁艂茞葨蒄蒭薂藯蜆螑蟼衟褑褠訐訔詖詗詪諈諑讌豗豷貗貣賯贋冱輀蒈轓迋逓鄺酳鈪尜鐐轷霘鞄騧髽魣鯀鰰鴹鼪龔秊䴔眮笀籣藑垲鍳鵬禔穯茿莂薃襛谻賚魳鵄㭎穄穵篛簑絭緅緍罇耑艒豠蹎辢醻鐍鑮闍頳驈髲鱮麰鼄鼅鼖㩳眣睎瞣矀硊碅磪礒禞秠穙穱窯竢笍筩篳簠粃粖糓糺紭紾絶綅繂繋繣罙罥罼羗羜翭耮聸肸胹脣腬膄膆膋臕舃艫艭艶艼荢荳萚蓗蓱蕋蕟薐薠藺蘓蘪虵蚾蛖蛜蝍蝨蟂蟜蠏衕衘袟袬誾譅譌譸讜趝趡跾踀踸蹡垌蹳躛躩躶軏軬輵轗轥逷遈邌鄟醎釭鈸怊銌鋂鋎鍐鎴鎸鑘閔雋膪霣靃韍颩飦餔駋騄骩骻骾鬙鬽魫鯈鯩鯬鰌鲓鴂鶍鶠鷁鷖鸇鸘鸧鹙麏黮齯龓盓眕睘睩矂矵矺砪硂碒磣祤禩稑穐穛竂笉篟篺紂紻綹緐縈繖繯繴纀羉翈耡腀艩苅莁菞菳萈蒁蒑蓔蓕蔙蔿蕧薆薗薝藀蘌虋蚿蜫蜽螥蠚袽裶裺褣褸詅詇詐誻諧謚豧貮賡賱赑赹赽踃蹞蹧躻躿輻郟鄑酼醁醕醥釪鈵銒銙鋺錗錥鍓鍟鎍鎘鏿鐎鐤鐿鑊锧閧闛隝隥隦靄靱鞪鞺鞿韟顀飀飥飪餒饆馿癀驦髉鬉鬸魛鳷鵋鵏鵨鵼鷵鷼鸍鸓鸖鹠黶鼉齰碀礇禪筣箏糧紐紳綀緱缾羷耊臚艍葏蠅詛誽諂賂輧輽釦鈕鏍鏽鐲颱饝騇髏腂臗眀砫祙祳粧蕣觓趹鄍鈡羭蝄衸謡閏盪眲睋矃矒硟碩磄礂礊祰祹禐秳秼稄稇稈稘稙穢竸竾笐笜筂箒箛箞箤箷箹箿篜簞簤簨簹簽籬粔粸紇紝紺絆絳綄綊綏綒綔綗綴緝緞緦緰緶縣縹繜繝繩纏罃罝罰羴翢聡聹聻聾脕脟脳脽脿臈艑艙艢芻茻荊菐菓菙菚菣菦菨葔葠葮葲蓙蔁蕛蕜蕦蕵蕷薖藨藮藰藳藵虃虘虜虝蛥蛶蜠蝸螐螖螡螢蟳蠌蠍蠒蠗蠝蠟袘褜褨襾覊覚覛覟覠覯訜訡訮証詷詺諉諒諘諦諺謀謠謩謸謽讍讛貦貸貽賅賊賳賺贀贄贊贌趪跁跈跒蹖軀軇軔軘軣軻輒輥輦轟逇邔邥邫鄽醆醞醽釥鈂鈽鉍鉛銓銜鋇鋒鋰鋷錠錦鎲鏈鏟鐑鐬鑲鑴鑿镻閑閰閳閴閹闌闡陮陻霂靵鞊鞛韓韴韷頊頋頓頜顕顨顴飷飺飾餀餌餓饒饡饳饻馴駜駣駥駨駶騰騿驁驇驑驕驖驥髞鬀鬄鬅鬢鬧魰魵魸魺鯊鯐鯓鯖鯗鰞鰬鰵鰸鰻鱌鱺鳩鳪鳶鴭鴳鴴鴵鴺鴽鵁鵝鶈鶐鶓鶩鶴鷩鷴鷽麩麵鼑鼘鼮齲齼龝䦃䲣䲠禖禵秅竌籙粵緋羠翖艣蚡訹諠輂輨遶鈆鈖銅鍥鎇绗鐷閽闟韮騣髧鴢鷘黺祶荮瞏稴笲笿縪纍翸肧臶蜸豊賁輐輘邏雘鯽䓖眞睴瞡砏磯粿紘舋葋薭虲蠩覵註詄譗趰軧岍鉼鋪鞻颵餼騍驂鯘鳿龎睉砤礑禰窤竈聶蕒説趌踄鑰隣饌驛骿鼥碵竤絒絓芼萢蓧蔄螦詀躦狨錋鎝鐩隲霝鞟礐禗稡穽糮羮肰艸葇葟蒪蝑螧蟅蟢貒銫関礤鮭鴙鴞鵣鵪鷦鷺齜盢眘瞞礿祩禨秺穟窫笎篨籋緤緵縚繿羙蘂蜼襘訞謄谼躒躭迍釿鏸颻餟餫餽驆鬳魒盉睱睻磠箋絣縀縛縧荙莕莙螠蟧襌襽豰賷鉽銲錧鍚鍱骣鑪靷頦騊骔魽魿鮅鮇鮎鮘鮪鯨鰿鱀鱄鱓鲖鴒')
  ])
]