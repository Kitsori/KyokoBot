import random
from collections import defaultdict

# The Huge List of Anime Girls - Grouped by shows listed on the right
girls = [
    (   #1                                                                             # Quintessential Quintuplets
     "Miku Nakano",
     "The Quintessential Quintuplets",
     "https://cdn.myanimelist.net/images/characters/14/457434.jpg"
    ),( #2
     "Nino Nakano",
     "The Quintessential Quintuplets",
     "https://cdn.myanimelist.net/images/characters/15/437486.jpg"
    ),(  #3
     "Itsuki Nakano",
     "The Quintessential Quintuplets",
     "https://cdn.myanimelist.net/images/characters/16/433646.jpg"
    ),(  #4
     "Yotsuba Nakano",
     "The Quintessential Quintuplets",
     "https://cdn.myanimelist.net/images/characters/10/433645.jpg"
    ),(  #5
     "Ichika Nakano",
     "The Quintessential Quintuplets",
     "https://cdn.myanimelist.net/images/characters/2/606471.jpg"
    ),(  #6
     "Raiha Uesugi",
     "The Quintessential Quintuplets",
     "https://cdn.myanimelist.net/images/characters/2/555613.jpg"
    ),(  #7                                                                             # 86 - Eighty Six
     "Vladilena Milize",
     "86 - Eighty Six",
     "https://cdn.myanimelist.net/images/characters/15/428175.jpg"
    ),(  #8
     "Anju Emma",
     "86 - Eighty Six",
     "https://cdn.myanimelist.net/images/characters/4/435464.jpg"
    ),(  #9
     "Kurena Kukumila",
     "86 - Eighty Six",
     "https://cdn.myanimelist.net/images/characters/13/435472.jpg"
    ),(  #10
     "Frederica Rosenfort",
     "86 - Eighty Six",
     "https://cdn.myanimelist.net/images/characters/10/453080.jpg"
    ),(  #11                                                                           # Angel Beats!
     "Kanade Tachibana",
     "Angel Beats!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423457496072327173/241395.png?"
    ),(  #12
     "Yuri Nakamura",
     "Angel Beats!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423457706395697253/91856.png?"
    ),(  #13
     "Yui",
     "Angel Beats!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423457779208687616/150391.png?"
    ),(  #14
     "Masami Iwasawa",
     "Angel Beats!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423457848767156334/117224.png?"
    ),(  #15
     "Shiina",
     "Angel Beats!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423457897727262863/110858.png?"
    ),(  #16                                                                            # Anohana
     "Meiko Honma",
     "Anohana",
     "https://media.discordapp.net/attachments/1423388983915708558/1423462507330273290/115711.png?"
    ),(  #17
     "Naruko Anjou",
     "Anohana",
     "https://media.discordapp.net/attachments/1423388983915708558/1423462558031024259/121622.png?"
    ),(  #18
     "Chiriko Tsurumi",
     "Anohana",
     "https://media.discordapp.net/attachments/1423388983915708558/1423462603048353913/118054.png?"
    ),(  #19                                                                             # Another
     "Mei Misaki",
     "Another",
     "https://media.discordapp.net/attachments/1423388983915708558/1423463685086515211/237389.png?"
    ),(  #20
     "Izumi Akazawa",
     "Another",
     "https://media.discordapp.net/attachments/1423388983915708558/1423463734763851796/155667.png?"
    ),(  #21                                                                             # Assassination Classroom
     "Kaede Kayano",
     "Assassination Classroom",
     "https://media.discordapp.net/attachments/1423388983915708558/1423464238667661377/274395.png?"
    ),(  #22
     "Irina Jelavic",
     "Assassination Classroom",
     "https://media.discordapp.net/attachments/1423388983915708558/1423464285304000523/276605.png?"
    ),(  #23
     "Rio Nakamura",
     "Assassination Classroom",
     "https://media.discordapp.net/attachments/1423388983915708558/1423464375758622770/277161.png?"
    ),(  #24
     "Ritsu Hayasaka",
     "Assassination Classroom",
     "https://media.discordapp.net/attachments/1423388983915708558/1423464319458480218/277977.png?"
    ),(  #25
     "Hinano Kurahashi",
     "Assassination Classroom",
     "https://media.discordapp.net/attachments/1423388983915708558/1423464411917451324/276606.png?"
    ),(  #26                                                                             # Arifureta
     "Yue",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423465491258933358/407199.png?"
    ),(  #27
     "Kaori Shirasaki",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423465944142839879/558844.png?"
    ),(  #28
     "Tio Klarus",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423465979198967868/371438.png?"
    ),(  #29
     "Shea Haulia",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423466020848533668/371437.png?"
    ),(  #30
     "Myuu",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423466055954600079/568863.png?"
    ),(  #31
     "Shizuku Yaegashi",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423466086895980667/402101.png?"
    ),(  #32
     "Suzu Taniguchi",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423466199261642752/568866.png?"
    ),(  #33
     "Liliana Heiligh",
     "Arifureta",
     "https://media.discordapp.net/attachments/1423388983915708558/1423466279372853539/480478.png?"
    ),(  #34                                                                            # Baka and Test
     "Minami Shimada",
     "Baka and Test",
     "https://media.discordapp.net/attachments/1423388983915708558/1423467612108750858/77138.png?"
    ),(  #35
     "Shouko Kirishima",
     "Baka and Test",
     "https://media.discordapp.net/attachments/1423388983915708558/1423467670506045581/96539.png?"
    ),(  #36
     "Mizuki Himeji",
     "Baka and Test",
     "https://media.discordapp.net/attachments/1423388983915708558/1423467712717520936/110667.png?"
    ),(  #37
     "Yuuko Kinoshita",
     "Baka and Test",
     "https://media.discordapp.net/attachments/1423388983915708558/1423467753427435521/76945.png?"
    ),(  #38
     "Akira Yoshii",
     "Baka and Test",
     "https://media.discordapp.net/attachments/1423388983915708558/1423467793222996009/85307.png?"
    ),(  #39                                                                            # Baan
     "Rinrada Ratchamanee",
     "Baan",
     "https://media.discordapp.net/attachments/1423388983915708558/1423468350050275398/598468.png?"
    ),(  #40                                                                            # BNA
     "Michiru Kagemori",
     "BNA",
     "https://media.discordapp.net/attachments/1423388983915708558/1423468715365896323/408681.png?"
    ),(  #41
     "Nazuna Hiwatashi",
     "BNA",
     "https://media.discordapp.net/attachments/1423388983915708558/1423468943095365694/367f5af87785e65cf6db80132cca0c0c.png?"
    ),(  #42                                                                            # Bocchi The Rock!
     "Hitori Gotou",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469539089453137/491455.png?"
    ),(  #43
     "Ryou Yamada",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469610660790454/544161.png?"
    ),(  #44
     "Nijika Ijichi",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469651987529779/544158.png?"
    ),(  #45
     "Kita Ikuyo",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469714004250715/495135.png?"
    ),(  #46
     "Kikuri Hiroi",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469756278640670/493846.png?"
    ),(  #47
     "PA-san",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469791397544049/502200.png?"
    ),(  #48
     "Seika Ijichi",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469833969864774/490794.png?"
    ),(  #49
     "Futari Gotou",
     "Bocchi The Rock!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423469872536490024/493791.png?"
    ),(  #50                                                                            # My Hero Academia
     "Ochako Uraraka",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471164650688674/309105.png?"
    ),(  #51
     "Himiko Toga",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471228454436915/485281.png?"
    ),(  #52
     "Tsuyu Asui",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471341851643997/343086.png?"
    ),(  #53
     "Kyouka Jirou",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471458050506762/309100.png?"
    ),(  #54
     "Momo Yaoyorozu",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471547712012398/562316.png?"
    ),(  #55
     "Mina Ashido",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471623817793651/329525.png?"
    ),(  #56
     "Nemuri Kayama",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471711717953708/366576.png?"
    ),(  #57
     "Tooru Hagakure",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471797382418452/301045.png?"
    ),(  #58
     "Mt. Lady",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423471852713545838/301651.png?"
    ),(  #59
     "Mei Hatsume",
     "My Hero Academia",
     "https://media.discordapp.net/attachments/1423388983915708558/1423472444617789512/517350.png?"
    ),(  #60                                                                              # BokuYaba
     "Anna Yamada",
     "The Dangers in My Heart",
     "https://media.discordapp.net/attachments/1423388983915708558/1423472864362758254/536836.png?"
    ),(  #61
     "Kana Ichikawa",
     "The Dangers in My Heart",
     "https://media.discordapp.net/attachments/1423388983915708558/1423472899393720430/578723.png?"
    ),(  #62
     "Moeko Sekine",
     "The Dangers in My Heart",
     "https://media.discordapp.net/attachments/1423388983915708558/1423472927940022424/569420.png?"
    ),(  #63
     "Chihiro Kobayashi",
     "The Dangers in My Heart",
     "https://media.discordapp.net/attachments/1423388983915708558/1423472954267664474/533899.png?"
    ),(  #64
     "Honoka Hara",
     "The Dangers in My Heart",
     "https://media.discordapp.net/attachments/1423388983915708558/1423472982096875582/533894.png?"
    ),(       #65                                                                            # Haganai
     "Sena Kashiwazaki",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473581630820352/132291.png?"
    ),(  #66
     "Yozora Mikazuki",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473639981842532/150969.png?"
    ),(  #67
     "Rika Shiguma",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473754541002802/198519.png?"
    ),(  #68
     "Kobato Hasegawa",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473696789495850/146645.png?"
    ),(  #69
     "Maria Takayama",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473786757451786/178131.png?"
    ),(  #70
     "Kate Takayama",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473896249884713/193475.png?"
    ),(  #71
     "Yukimura Kusunoki",
     "Haganai",
     "https://media.discordapp.net/attachments/1423388983915708558/1423473835419635722/205391.png?"
    ),(  #72                                                                            # Bubble
     "Uta",
     "Bubble",
     "https://media.discordapp.net/attachments/1423388983915708558/1423474993659908147/466809.png?"
    ),(  #73                                                                            # Chainsaw Man
     "Power",
     "Chainsaw Man",
     "https://media.discordapp.net/attachments/1423388983915708558/1423475566706954341/494969.png?"
    ),(  #74
     "Makima",
     "Chainsaw Man",
     "https://media.discordapp.net/attachments/1423388983915708558/1423475614886662154/494972.png?"
    ),(  #75
     "Reze",
     "Chainsaw Man",
     "https://media.discordapp.net/attachments/1423388983915708558/1423475660868812820/574771.png?"
    ),(  #76
     "Kobeni Higashiyama",
     "Chainsaw Man",
     "https://media.discordapp.net/attachments/1423388983915708558/1423475693504827422/533497.png?"
    ),(  #77
     "Himeno",
     "Chainsaw Man",
     "https://media.discordapp.net/attachments/1423388983915708558/1423475724190224455/492411.png?"
    ),(  #78                                                                            # Charlotte
     "Nao Tomori",
     "Charlotte",
     "https://media.discordapp.net/attachments/1423388983915708558/1423476465886036079/288019.png?"
    ),(  #79
     "Ayumi Otosaka",
     "Charlotte",
     "https://media.discordapp.net/attachments/1423388983915708558/1423476554528194580/288021.png?"
    ),(  #80
     "Yusa Kurobane",
     "Charlotte",
     "https://media.discordapp.net/attachments/1423388983915708558/1423476637483139092/288018.png?"
    ),(  #81
     "Misa Kurobane",
     "Charlotte",
     "https://media.discordapp.net/attachments/1423388983915708558/1423476679682293862/341989.png?"
    ),(  #82                                                                            # CLANNAD
     "Nagisa Furukawa",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484016136556614/300961.png?"
    ),(  #83
     "Ushio Okazaki",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484059186892899/382211.png?"
    ),(  #84
     "Tomoyo Sakagami",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484104355221525/34293.png?"
    ),(  #85
     "Kyou Fujibayashi",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484184034283551/70221.png?"
    ),(  #86
     "Fuuko Ibuki",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484237021057064/79593.png?"
    ),(  #87
     "Kotomi Ichinose",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484310564110427/79587.png?"
    ),(  #88
     "Sanae Furukawa",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484356365652130/54058.png?"
    ),(  #89
     "Ryou Fujibayashi",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484391413518386/256501.png?"
    ),(  #90
     "Mei Sunohara",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484431695347765/35087.png?"
    ),(  #91
     "Misae Sagara",
     "CLANNAD",
     "https://media.discordapp.net/attachments/1423388983915708558/1423484470576680991/382201.png?"
    ),(  #92
     "Lucy",
     "Cyberpunk: Edgerunners",
     "https://media.discordapp.net/attachments/1423388983915708558/1423485741962362911/486620.png?"
    ),(  #93
     "Rebecca",
     "Cyberpunk: Edgerunners",
     "https://media.discordapp.net/attachments/1423388983915708558/1423485801727135924/547499.png?"
    ),(  #94
     "Momo Ayase",
     "Dandadan",
     "https://media.discordapp.net/attachments/1423388983915708558/1423495325821440171/562295.png?"
    ),(  #95
     "Aira Shiratori",
     "Dandadan",
     "https://media.discordapp.net/attachments/1423388983915708558/1423495373804011610/569271.png?"
    ),(  #96
     "Seiko Ayase",
     "Dandadan",
     "https://media.discordapp.net/attachments/1423388983915708558/1423495423947178024/541026.png?"
    ),(  #97
     "Turbo Granny",
     "Dandadan",
     "https://media.discordapp.net/attachments/1423388983915708558/1423495479114731530/510909.png?"
    ),(  #98
     "Vamola",
     "Dandadan",
     "https://media.discordapp.net/attachments/1423388983915708558/1423495909177819207/605981.png?"
    ),(  #99
     "Yoshino Himekawa",
     "Date a Live",
     "https://media.discordapp.net/attachments/1422438714730217482/1423060152835248341/Yoshino.jpg?"
    ),(  #100
     "Mukuro Hoshimiya",
     "Date a Live",
     "https://media.discordapp.net/attachments/1422999881269645424/1423058083743137905/Mukuro_Hoshimiya.jpg?"
    ),(  #101
     "Kurumi Tokisaki",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497322888695888/468511.png?"
    ),(  #102
     "Tohka Yatogami",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497462017949706/202193.png?"
    ),(  #103
     "Origami Tobiichi",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497542020104273/202609.png?"
    ),(  #104
     "Kotori Itsuka",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497606113529898/211505.png?"
    ),(  #105
     "Miku Izayoi",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497652351406240/263775.png?"
    ),(  #106
     "Natsumi Kyouno",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497740586975275/551485.png?"
    ),(  #107
     "Yuzuru Yamai",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497829208428584/249039.png?"
    ),(  #108
     "Kaguya Yamai",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497871461978265/249041.png?"
    ),(  #109
     "Reine Murasame",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423497950482399324/209483.png?"
    ),(  #110
     "Mio Takamiya",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423498059639164958/491024.png?"
    ),(  #111
     "Nia Honjou",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423498105252220990/577849.png?"
    ),(  #112
     "Mana Takamiya",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423498314841722910/209869.png?"
    ),(  #113
     "Mii Fujibakama",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423498341106585631/211899.png?"
    ),(  #114
     "Nibelcole",
     "Date a Live",
     "https://media.discordapp.net/attachments/1423388983915708558/1423498418180980827/476933.png?"
    ),(  #115
     "Yua Serufu",
     "Do It Yourself!!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423500525932118126/494673.png?"
    ),(  #116
     "Jobko",
     "Do It Yourself!!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423500563164827708/493799.png?"
    ),(  #117
     "Kokoro Kouki",
     "Do It Yourself!!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423500599365992498/493797.png?"
    ),(  #118
     "Miku Suride",
     "Do It Yourself!!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423500631884169298/493219.png?"
    ),(  #119
     "Rei Yasaku",
     "Do It Yourself!!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423500660975997009/511856.png?"
    ),(  #120
     "Takumi Hikage",
     "Do It Yourself!!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423500687622275092/511857.png?"
    ),(  #121
     "Rui Tachibana",
     "Domestic Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423501229748785203/382489.png?"
    ),(  #122
     "Hina Tachibana",
     "Domestic Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423501271184441489/385149.png?"
    ),(  #123
     "Marcille Donato",
     "Dungeon Meshi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423501894411616357/512503.png?"
    ),(  #124
     "Izutsumi",
     "Dungeon Meshi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423501936199598150/543860.png?"
    ),(  #125
     "Falin Touden",
     "Dungeon Meshi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423501995691606037/543864.png?"
    ),(  #126
     "Namari",
     "Dungeon Meshi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423502057666773093/543865.png?"
    ),(  #127
     "Inutade",
     "Dungeon Meshi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423502081909723236/543788.png?"
    ),(  #128
     "Hestia",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423503577623560312/285883.png?"
    ),(  #129
     "Ais Wallenstein",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423503672821940325/512524.png?"
    ),(  #130
     "Ryuu Lion",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423503731491868694/508899.png?"
    ),(  #131
     "Liliruca Arde",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423503785107525764/285907.png?"
    ),(  #132
     "Freya",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423503863406788698/568506.png?"
    ),(  #133
     "Mikoto Yamato",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423503917639270400/508902.png?"
    ),(  #134
     "Syr Flova",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504048551891035/382146.png?"
    ),(  #135
     "Eina Tulle",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504122639814787/281237.png?"
    ),(  #136
     "Hephaistos",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504184849858641/512539.png?"
    ),(  #137
     "Asufi Al Andromeda",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504370162733149/390544.png?"
    ),(  #138
     "Loki",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504444640858132/512525.png?"
    ),(  #139
     "Tione Hiryute",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504514195132506/328384.png?"
    ),(  #140
     "Tiona Hiryute",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504569044045835/508897.png?"
    ),(  #141
     "Haruhime Sanjouno",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504627437011044/508901.png?"
    ),(  #142
     "Wiene",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504681497530430/501677.png?"
    ),(  #143
     "Aisha Belka",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504728922525786/508894.png?"
    ),(  #144
     "Chigusa Hitachi",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504791354740746/508886.png?"
    ),(  #145
     "Cassandra Ilion",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504852222476288/508888.png?"
    ),(  #146
     "Anya Flomer",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504909101170840/285143.png?"
    ),(  #147
     "Chloe Lolo",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423504956756852868/563882.png?"
    ),(  #148
     "Daphne Rauros",
     "Danmachi",
     "https://media.discordapp.net/attachments/1423388983915708558/1423505000419688519/508887.png?"
    ),(  #149
     "Tamaki Kotatsu",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423506733866811412/496649.png?"
    ),(  #150
     "Maki Oze",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423506806050783334/568634.png?"
    ),(  #151
     "Iris",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423506846458839161/587867.png?"
    ),(  #152
     "Hibana",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423506905669828638/550253.png?"
    ),(  #153
     "Haumea",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423506938087346237/587876.png?"
    ),(  #154
     "Lisa Isaribe",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423506978155528213/587869.png?"
    ),(  #155
     "Inca Kasugatani",
     "Fire Force",
     "https://media.discordapp.net/attachments/1423388983915708558/1423507005615771830/417617.png?"
    ),(  #156
     "Kisara",
     "Engage Kiss",
     "https://media.discordapp.net/attachments/1423388983915708558/1423507703669592135/495138.png?"
    ),(  #157
     "Ayano Yuugiri",
     "Engage Kiss",
     "https://media.discordapp.net/attachments/1423388983915708558/1423507754429190226/472531.png?"
    ),(  #158
     "Sharon Holygrail",
     "Engage Kiss",
     "https://media.discordapp.net/attachments/1423388983915708558/1423507780303585433/476675.png?"
    ),(  #159
     "Kanna Ogata",
     "Engage Kiss",
     "https://media.discordapp.net/attachments/1423388983915708558/1423507807465902100/487693.png?"
    ),(  #160
     "Takuhaigyousha",
     "Engage Kiss",
     "https://media.discordapp.net/attachments/1423388983915708558/1423507834733199360/481323.png?"
    ),(  #161
     "Sagiri Izumi",
     "Eromanga Sensei",
     "https://media.discordapp.net/attachments/1423388983915708558/1423508265916039310/327378.png?"
    ),(  #162
     "Elf Yamada",
     "Eromanga Sensei",
     "https://media.discordapp.net/attachments/1423388983915708558/1423508296408760330/330038.png?"
    ),(  #163
     "Megumi Jinno",
     "Eromanga Sensei",
     "https://media.discordapp.net/attachments/1423388983915708558/1423508323994570822/327003.png?"
    ),(  #164
     "Muramasa Senju",
     "Eromanga Sensei",
     "https://media.discordapp.net/attachments/1423388983915708558/1423508356571594865/333305.png?"
    ),(  #165
     "Tomoe Takasago",
     "Eromanga Sensei",
     "https://media.discordapp.net/attachments/1423388983915708558/1423508382823874560/324564.png?"
    ),(  #166
     "Saber",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423509644483104878/315100.png?"
    ),(  #167
     "Rin Tohsaka",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423509790457462855/270529.png?"
    ),(  #168
     "Illyasviel von Einzbern",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423509870577188884/345110.png?"
    ),(  #169
     "Caster",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423509911718989894/128797.png?"
    ),(  #170
     "Luviagelita Edelfelt",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423509953200652318/503811.png?"
    ),(  #171
     "Taiga Fujimura",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423509991842648114/275651.png?"
    ),(  #172
     "Ayako Mitsuzuri",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423510031583674378/296248.png?"
    ),(  #173
     "Sakura Matou",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423510132603621376/294277.png?"
    ),(  #174
     "Rider",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423510335800741908/341407.png?"
    ),(  #175
     "Irisviel von Einzbern",
     "Fate",
     "https://media.discordapp.net/attachments/1423388983915708558/1423510397608136815/112995.png?"
    ),(  #176
     "Haruko Haruhara",
     "FLCL",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511425678311464/523359.png?"
    ),(  #177
     "Mamimi Samejima",
     "FLCL",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511492283727892/218999.png?"
    ),(  #178
     "Eri Ninamori",
     "FLCL",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511517306945576/33201.png?"
    ),(  #179
     "Papika",
     "Flip Flappers",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511818239873096/316263.png?"
    ),(  #180
     "Cocona Cocomine",
     "Flip Flappers",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511849793618030/316264.png?"
    ),(  #181
     "Yayaka",
     "Flip Flappers",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511876368859137/313367.png?"
    ),(  #182
     "Yuyu",
     "Flip Flappers",
     "https://media.discordapp.net/attachments/1423388983915708558/1423511902461624362/525861.png?"
    ),(  #183
     "Tohru Honda",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512665191350272/378748.png?"
    ),(  #184
     "Saki Hanajima",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512723299369050/401128.png?"
    ),(  #185
     "Isuzu Souma",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512772565794887/449502.png?"
    ),(  #186
     "Akito Souma",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512801732726835/410560.png?"
    ),(  #187
     "Kisa Souma",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512825313230929/410557.png?"
    ),(  #188
     "Kyouko Honda",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512851993067561/400004.png?"
    ),(  #189
     "Arisa Uotani",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512892917026897/410559.png?"
    ),(  #190
     "Machi Kuragi",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512926811066470/419508.png?"
    ),(  #191
     "Kagura Souma",
     "Fruits Basket",
     "https://media.discordapp.net/attachments/1423388983915708558/1423512966673727559/413950.png?"
    ),(  #192
     "Riza Hawkeye",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514178403958794/451785.png?"
    ),(  #193
     "Winry Rockbell",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514316342300822/527339.png?"
    ),(  #194
     "Olivier Armstrong",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514367294443583/83953.png?"
    ),(  #195
     "Izumi Curtis",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514405223796868/85257.png?"
    ),(  #196
     "Lust",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514443953999934/76639.png?"
    ),(  #197
     "Mei Chang",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514485070499910/572516.png?"
    ),(  #198
     "Trisha Elric",
     "Fullmetal Alchemist",
     "https://media.discordapp.net/attachments/1423388983915708558/1423514751564124201/59741.png?"
    ),(  #199
     "Akari Watanabe",
     "More Than A Married Couple, But Not Lovers",
     "https://media.discordapp.net/attachments/1423388983915708558/1423515152925458462/499736.png?"
    ),(  #200
     "Shiori Sakurazaka",
     "More Than A Married Couple, But Not Lovers",
     "https://media.discordapp.net/attachments/1423388983915708558/1423515196676116590/525158.png?"
    ),(  #201
     "Gabriel Tenma White",
     "Gabriel Dropout",
     "https://media.discordapp.net/attachments/1423388983915708558/1423516522667573318/310289.png?"
    ),(  #202
     "Satanichia Kurumizawa McDowell",
     "Gabriel Dropout",
     "https://media.discordapp.net/attachments/1423388983915708558/1423516568494805012/339560.png?"
    ),(  #203
     "Vignette Tsukinose April",
     "Gabriel Dropout",
     "https://media.discordapp.net/attachments/1423388983915708558/1423516601650647172/310288.png?"
    ),(  #204
     "Raphiel Shiraha Ainsworth",
     "Gabriel Dropout",
     "https://media.discordapp.net/attachments/1423388983915708558/1423516634030538822/310287.png?"
    ),(  #205
     "Tapris Sugarbell Chisaki",
     "Gabriel Dropout",
     "https://media.discordapp.net/attachments/1423388983915708558/1423516656440709130/326345.png?"
    ),(  #206
     "Kurumi Ebisuzawa",
     "School Live!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517351562711152/292298.png?"
    ),(  #207
     "Yuki Takeya",
     "School Live!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517416817692742/314213.png?"
    ),(  #208
     "Miki Naoki",
     "School Live!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517462229422191/292297.png?"
    ),(  #209
     "Yuuri Wakasa",
     "School Live!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517512502345729/304875.png?"
    ),(  #210
     "Megumi Sakura",
     "School Live!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517544131723325/287734.png?"
    ),(  #211
     "Nina Iseri",
     "Girls Band Cry",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517967957753996/578487.png?"
    ),(  #212
     "Subaru Awa",
     "Girls Band Cry",
     "https://media.discordapp.net/attachments/1423388983915708558/1423517996013584445/578489.png?"
    ),(  #213
     "Momoko Kawaragi",
     "Girls Band Cry",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518026141274164/512880.png?"
    ),(  #214
     "Rupa",
     "Girls Band Cry",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518048362434631/512877.png?"
    ),(  #215
     "Tomo Ebizuka",
     "Girls Band Cry",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518069330018406/512881.png?"
    ),(  #216
     "Inori Yuzuriha",
     "Guilty Crown",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518512344862795/139621.png?"
    ),(  #217
     "Ayase Shinomiya",
     "Guilty Crown",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518550785654814/136733.png?"
    ),(  #218
     "Tsugumi",
     "Guilty Crown",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518627247689798/137319.png?"
    ),(  #219
     "Hare Menjou",
     "Guilty Crown",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518676421967892/137325.png?"
    ),(  #220
     "Mana Ouma",
     "Guilty Crown",
     "https://media.discordapp.net/attachments/1423388983915708558/1423518718687707196/150755.png?"
    ),(  #221
     "Satou Matsuzaka",
     "Happy Sugar Life",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519223329853450/363439.png?"
    ),(  #222
     "Shio Koube",
     "Happy Sugar Life",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519265998508172/427428.png?"
    ),(  #223
     "Shouko Hida",
     "Happy Sugar Life",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519294729224306/363523.png?"
    ),(  #224
     "Satou's Aunt",
     "Happy Sugar Life",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519334084378718/363441.png?"
    ),(  #225
     "Tsutsuji Higa",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519918581616700/585073.png?"
    ),(  #226
     "Mako Kawai",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519940291330118/585068.png?"
    ),(  #227
     "Kurea Furutachi",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519964190736525/585069.png?"
    ),(  #228
     "Nana Hoshi",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423519993244422216/585074.png?"
    ),(  #229
     "Shinon Ogawa",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423520015826681997/585070.png?"
    ),(  #230
     "Mayumi Oota",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423520039365120100/590025.png?"
    ),(  #231
     "Sakura Kodama",
     "Food for the Soul",
     "https://media.discordapp.net/attachments/1423388983915708558/1423520058159927326/594971.png?"
    ),(  #232
     "Kumiko Oumae",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423522426628735016/316261.png?"
    ),(  #233
     "Reina Kousaka",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423522514688020612/555742.png?"
    ),(  #234
     "Hazuki Katou",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423522568274706452/301152.png?"
    ),(  #235
     "Sapphire Kawashima",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423522857832550450/282019.png?"
    ),(  #236
     "Asuka Tanaka",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423522930351931432/319400.png?"
    ),(  #237
     "Mizore Yoroizuka",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423522984693469324/318491.png?"
    ),(  #238
     "Natsuki Nakagawa",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523044290465923/295718.png?"
    ),(  #239
     "Nozomi Kasaki",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523077291118642/316295.png?"
    ),(  #240
     "Yuuko Yoshikawa",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523128122015804/286735.png?"
    ),(  #241
     "Haruka Ogasawara",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523169914064996/280131.png?"
    ),(  #242
     "Kaori Nakaseko",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523213861715968/284932.png?"
    ),(  #243
     "Mamiko Oumae",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523266655686739/285033.png?"
    ),(  #244
     "Kanade Hisaishi",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523304425132086/545007.png?"
    ),(  #245
     "Mayu Kuroe",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523425040863334/544505.png?"
    ),(  #246
     "Satsuki Suzuki",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523453495021578/438564.png?"
    ),(  #247
     "Mirei Suzuki",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523481970282588/424974.png?"
    ),(  #248
     "Yayoi Kamiishi",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523629534281859/b330332-WQ9sA8zL6F49.png?"
    ),(  #249
     "Suzume Kamaya",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523718407389204/b330331-b3TjqW6mZn9T.png?"
    ),(  #250
     "Sari Yoshii",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523758248824983/545009.png?"
    ),(  #251
     "Tsubame Kamaya",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523783859376129/508226.png?"
    ),(  #252
     "Azusa Sasaki",
     "Sound! Euphonium",
     "https://media.discordapp.net/attachments/1423388983915708558/1423523811642441738/390747.png?"
    ),(  #253
     "Sayu Ogiwara",
     "Higehiro",
     "https://media.discordapp.net/attachments/1423388983915708558/1423525013214072914/444114.png?"
    ),(  #254
     "Yuzuha Mishima",
     "Higehiro",
     "https://media.discordapp.net/attachments/1423388983915708558/1423525051369652324/420042.png?"
    ),(  #255
     "Airi Gotou",
     "Higehiro",
     "https://media.discordapp.net/attachments/1423388983915708558/1423525071380549742/420039.png?"
    ),(  #256
     "Asami Yuuki",
     "Higehiro",
     "https://media.discordapp.net/attachments/1423388983915708558/1423525092050337894/420041.png?"
    ),(  #257
     "Umika Konohoshi",
     "Stardust Telepath",
     "https://media.discordapp.net/attachments/1423388983915708558/1423550871723180042/519887.png?"
    ),(  #258
     "Yuu Akeuchi",
     "Stardust Telepath",
     "https://media.discordapp.net/attachments/1423388983915708558/1423550912991068200/519888.png?"
    ),(  #259
     "Matataki Raimon",
     "Stardust Telepath",
     "https://media.discordapp.net/attachments/1423388983915708558/1423550944225919009/519889.png?"
    ),(  #260
     "Haruno Takaragi",
     "Stardust Telepath",
     "https://media.discordapp.net/attachments/1423388983915708558/1423550967374286878/519890.png?"
    ),(  #261
     "Sophie Hatter",
     "Howl's Moving Castle",
     "https://media.discordapp.net/attachments/1423388983915708558/1423551373097570324/102657.png?"
    ),(  #262
     "Nayuta Kani",
     "A Sister's All You Need.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423551665574907975/338865.png?"
    ),(  #263
     "Miyako Shirakawa",
     "A Sister's All You Need.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423551702669201469/338866.png?"
    ),(  #264
     "Ashley Oono",
     "A Sister's All You Need.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423551744910163979/342666.png?"
    ),(  #265
     "Josee",
     "Josee, The Tiger and the Fish",
     "https://media.discordapp.net/attachments/1423388983915708558/1423552010338304132/441918.png?"
    ),(  #266
     "Yui Hirasawa",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555071764856903/326131.png?"
    ),(  #267
     "Mio Akiyama",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555146310357174/48547.png?"
    ),(  #268
     "Azusa Nakano",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555213452775434/86736.png?"
    ),(  #269
     "Tsumugi Kotobuki",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555268834496593/48550.png?"
    ),(  #270
     "Ritsu Tainaka",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555330469531738/51212.png?"
    ),(  #271
     "Ui Hirasawa",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555396102262864/83872.png?"
    ),(  #272
     "Sawako Yamanaka",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555493049143376/48577.png?"
    ),(  #273
     "Nodoka Manabe",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555561844113429/80300.png?"
    ),(  #274
     "Jun Suzuki",
     "K-ON!",
     "https://media.discordapp.net/attachments/1423388983915708558/1423555602319147019/95854.png?"
    ),(  #275
     "Kaguya Shinomiya",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423556981393719326/504723.png?"
    ),(  #276
     "Chika Fujiwara",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423557063409275042/406395.png?"
    ),(  #277
     "Miko Iino",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423557166798868542/600330.png?"
    ),(  #278
     "Ai Hayasaka",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423557257995747349/504012.png?"
    ),(  #279
     "Kei Shirogane",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423557294570078288/395331.png?"
    ),(  #280
     "Maki Shijou",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423557322503880794/409888.png?"
    ),(  #281
     "Tsubame Koyasu",
     "Kaguya-sama: Love is War",
     "https://media.discordapp.net/attachments/1423388983915708558/1423557385087225866/568203.png?"
    ),(  #282
     "Kikoru Shinomiya",
     "Kaiju No. 8",
     "https://media.discordapp.net/attachments/1423388983915708558/1423558061754159146/549659.png?"
    ),(  #283
     "Mina Ashiro",
     "Kaiju No. 8",
     "https://media.discordapp.net/attachments/1423388983915708558/1423558097980493918/531193.png?"
    ),(  #284
     "Konomi Okonogi",
     "Kaiju No. 8",
     "https://media.discordapp.net/attachments/1423388983915708558/1423558123486056469/553884.png?"
    ),(  #285
     "Rin Shinonome",
     "Kaiju No. 8",
     "https://media.discordapp.net/attachments/1423388983915708558/1423558149121638400/599682.png?"
    ),(  #286
     "Chizuru Ichinose",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423558632183959602/484261.png?"
    ),(  #287
     "Sumi Sakurasawa",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423558714769670174/484263.png?"
    ),(  #288
     "Ruka Sarashina",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423559018835873942/484264.png?"
    ),(  #289
     "Mami Nanami",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423559099404128308/484262.png?"
    ),(  #290
     "Mini Yaemori",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423559145709109358/560760.png?"
    ),(  #291
     "Sayuri Ichinose",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423559172032696402/414333.png?"
    ),(  #292
     "Nagomi Kinoshita",
     "Rent a Girlfriend",
     "https://media.discordapp.net/attachments/1423388983915708558/1423559195810332723/409379.png?"
    ),(  #293
     "Ayu Tsukimiya",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560301302775869/33327.png?"
    ),(  #294
     "Mai Kawasumi",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560363240329299/33326.png?"
    ),(  #295
     "Makoto Sawatari",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560403169968128/79216.png?"
    ),(  #296
     "Nayuki Minase",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560432911650866/32976.png?"
    ),(  #297
     "Shiori Misaka",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560488901415024/81057.png?"
    ),(  #298
     "Sayuri Kurata",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560534866923602/32980.png?"
    ),(  #299
     "Akiko Minase",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560578420572240/39463.png?"
    ),(  #300
     "Kaori Misaka",
     "Kanon",
     "https://media.discordapp.net/attachments/1423388983915708558/1423560616911573063/75633.png?"
    ),(  #301
     "Kaoruko Waguri",
     "The Fragrant Flower Blooms With Dignity",
     "https://media.discordapp.net/attachments/1423388983915708558/1423562725644173343/image.png?"
    ),(  #302
     "Subaru Hoshina",
     "The Fragrant Flower Blooms With Dignity",
     "https://media.discordapp.net/attachments/1423388983915708558/1423562915574972506/603882.png?"
    ),(  #303
     "Kyouko Tsumugi",
     "The Fragrant Flower Blooms With Dignity",
     "https://media.discordapp.net/attachments/1423388983915708558/1423562942980558871/599660.png?"
    ),(  #304
     "Madoka Yuzuhara",
     "The Fragrant Flower Blooms With Dignity",
     "https://media.discordapp.net/attachments/1423388983915708558/1423562990451556412/506588.png?"
    ),(  #305
     "Nezuko Kamado",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564341222965308/495381.png?"
    ),(  #306
     "Shinobu Kochou",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564382927061012/386591.png?"
    ),(  #307
     "Mitsuri Kanroji",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564424618180608/502282.png?"
    ),(  #308
     "Kanao Tsuyuri",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564457325494282/384712.png?"
    ),(  #309
     "Tamayo",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564501277610044/384692.png?"
    ),(  #310
     "Kanae Kochou",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564527546400818/389355.png?"
    ),(  #311
     "Aoi Kanzaki",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564625521410110/388816.png?"
    ),(  #312
     "Daki",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564677623058563/526179.png?"
    ),(  #313
     "Suma",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564735399460894/464879.png?"
    ),(  #314
     "Makio",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564773471027260/459853.png?"
    ),(  #315
     "Hinatsuru",
     "Demon Slayer",
     "https://media.discordapp.net/attachments/1423388983915708558/1423564806530797679/459860.png?"
    ),(  #316
     "Karane Inda",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1422999881269645424/1423055211374579742/Karane_Inda.jpg?"
    ),(  #317
     "Shizuka Yoshimoto",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423565996786192435/525015.png?"
    ),(  #318
     "Nano Eiai",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566024636104814/525017.png?"
    ),(  #319
     "Hakari Hanazono",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566065056747540/525016.png?"
    ),(  #320
     "Kusuri Yakuzen",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566095411052555/525018.png?"
    ),(  #321
     "Hahari Hanazono",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566129497899078/534187.png?"
    ),(  #322
     "Kurumi Haraga",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566173970235452/578045.png?"
    ),(  #323
     "Mei Meido",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566205641560095/578043.png?"
    ),(  #324
     "Iku Sutou",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566233936203858/574207.png?"
    ),(  #325
     "Meme Kakure",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566265494016101/552156.png?"
    ),(  #326
     "Mimimi Utsukushisugi",
     "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566346343546980/571775.png?"
    ),(  #327
     "Mitsuha Miyamizu",
     "Your Name",
     "https://media.discordapp.net/attachments/1423388983915708558/1423566852784918619/336342.png?"
    ),(  #328
     "Isaki Magari",
     "Insomniacs After School",
     "https://media.discordapp.net/attachments/1423388983915708558/1423567402351857764/499097.png?"
    ),(  #329
     "Yui Shiromaru",
     "Insomniacs After School",
     "https://media.discordapp.net/attachments/1423388983915708558/1423567443967742072/499066.png?"
    ),(  #330
     "Motoko Kanikawa",
     "Insomniacs After School",
     "https://media.discordapp.net/attachments/1423388983915708558/1423567480852447333/499069.png?"
    ),(  #331
     "Kanami Anamizu",
     "Insomniacs After School",
     "https://media.discordapp.net/attachments/1423388983915708558/1423567512351539311/499068.png?"
    ),(  #332
     "Haya Magari",
     "Insomniacs After School",
     "https://media.discordapp.net/attachments/1423388983915708558/1423567541959397446/512982.png?"
    ),(  #333
     "Mina Nono",
     "Insomniacs After School",
     "https://media.discordapp.net/attachments/1423388983915708558/1423567576533041153/499070.png?"
    ),(  #334
     "Kobato Hanato",
     "Kobato.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423568373484224563/49333.png?"
    ),(  #335
     "Kohaku",
     "Kobato.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423568424180912251/64545.png?"
    ),(  #336
     "Chiho Mihara",
     "Kobato.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423568454514114560/81352.png?"
    ),(  #337
     "Chise Mihara",
     "Kobato.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423568483354017873/81356.png?"
    ),(  #338
     "Sayaka Okiura",
     "Kobato.",
     "https://media.discordapp.net/attachments/1423388983915708558/1423568533031223357/81372.png?"
    ),(  #339
     "Kanna Kamui",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569112894017618/584701.png?"
    ),(  #340
     "Tohru",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569160767672330/456435.png?"
    ),(  #341
     "Kobayashi",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569214920462416/456442.png?"
    ),(  #342
     "Lucoa",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569302396600444/322912.png?"
    ),(  #343
     "Elma",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569393652338689/456447.png?"
    ),(  #344
     "Ilulu",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569520617979945/529025.png?"
    ),(  #345
     "Riko Saikawa",
     "Miss Kobayashi's Dragon Maid",
     "https://media.discordapp.net/attachments/1423388983915708558/1423569557091782716/323304.png?"
    ),(  #346
     "Shouko Komi",                                                                         # Komi Can't Communicate
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/10/452353.jpg"
    ),(  #347
     "Kaede Otori",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/2/455023.jpg"
    ),(  #348
     "Nene Onemine",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/15/486159.jpg"
    ),(  #349
     "Omoharu Nakanaka",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/12/451436.jpg"
    ),(  #350
     "Shuuko Komi",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/2/522134.jpg"
    ),(  #351
     "Himiko Agari",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/10/451435.jpg"
    ),(  #352
     "Ren Yamai",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/6/451763.jpg"
    ),(  #353
     "Hitomi Tadano",
     "Komi Can't Communicate",
     "https://cdn.myanimelist.net/images/characters/12/453351.jpg"
    ),(  #354
     "Megumin",                                                                               # Konosuba
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/2/309075.jpg"
    ),(  #355
     "Aqua",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/13/327741.jpg"
    ),(  #356
     "Darkness",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/7/301407.jpg"
    ),(  #357
     "Wiz",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/14/312300.jpg"
    ),(  #358
     "Yunyun",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/13/583284.jpg"
    ),(  #359
     "Eris",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/3/397294.jpg"
    ),(  #360
     "Chris",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/3/303916.jpg"
    ),(  #361
     "Iris Stylish-Sword Belzerg",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/6/546088.jpg"
    ),(  #362
     "Luna",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/6/304985.jpg"
    ),(  #363
     "Sylvia",
     "Konosuba",
     "https://cdn.myanimelist.net/images/characters/3/577577.jpg"
    ),(  #364
     "Hana Haruyama",                                                                       # Flower and Asura
     "Flower and Asura",
     "https://cdn.myanimelist.net/images/characters/6/586012.jpg"
    ),(  #365
     "Mizuki Usurai",
     "Flower and Asura",
     "https://cdn.myanimelist.net/images/characters/4/586013.jpg"
    ),(  #366
     "An Natsue",
     "Flower and Asura",
     "https://cdn.myanimelist.net/images/characters/13/586015.jpg"
    ),(  #367
     "Ryouko Totonoi",
     "Flower and Asura",
     "https://cdn.myanimelist.net/images/characters/16/586010.jpg"
    ),(  #368
     "Nagisa Kubo",                                                                         # Kubo Won't Let Me Be Invisible
     "Kubo Won't Let Me Be Invisible",
     "https://cdn.myanimelist.net/images/characters/13/473602.jpg"
    ),(  #369
     "Akina Kubo",
     "Kubo Won't Let Me Be Invisible",
     "https://cdn.myanimelist.net/images/characters/4/493275.jpg"
    ),(  #370
     "Saki Kubo",
     "Kubo Won't Let Me Be Invisible",
     "https://cdn.myanimelist.net/images/characters/13/493276.jpg"
    ),(  #371
     "Hazuki Kudou",
     "Kubo Won't Let Me Be Invisible",
     "https://cdn.myanimelist.net/images/characters/10/493277.jpg"
    ),(  #372
     "Yoshie Shiraishi",
     "Kubo Won't Let Me Be Invisible",
     "https://cdn.myanimelist.net/images/characters/8/495979.jpg"
    ),(  #373
     "Tamao Taira",
     "Kubo Won't Let Me Be Invisible",
     "https://cdn.myanimelist.net/images/characters/5/493278.jpg"
    ),(  #374
     "Maomao",                                                                              # The Apothecary Diaries
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/11/516703.jpg"
    ),(  #375
     "Loulan",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/8/592718.jpg"
    ),(  #376
     "Gyokuyou",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/7/525779.jpg"
    ),(  #377
     "Shisui",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/12/574074.jpg"
    ),(  #378
     "Xiaolan",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/16/574075.jpg"
    ),(  #379
     "Lihua",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/9/574071.jpg"
    ),(  #380
     "Ah-Duo",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/16/530561.jpg"
    ),(  #381
     "Meimei",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/9/533407.jpg"
    ),(  #382
     "Pairin",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/13/525778.jpg"
    ),(  #383
     "Lishu",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/10/574072.jpg"
    ),(  #384
     "Suirei",
     "The Apothecary Diaries",
     "https://cdn.myanimelist.net/images/characters/2/591772.jpg"
    ),(  #385
     "Rin Natsume",                                                                         # Little Busters!
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/3/182839.jpg"
    ),(  #386
     "Kudryavka Noumi",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/3/178971.jpg"
    ),(  #387
     "Yuiko Kurugaya",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/11/229813.jpg"
    ),(  #388
     "Komari Kamikita",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/13/186201.jpg"
    ),(  #389
     "Haruka Saigusa",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/10/186205.jpg"
    ),(  #390
     "Mio Nishizono",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/10/186203.jpg"
    ),(  #391
     "Kanata Futaki",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/8/212731.jpg"
    ),(  #392
     "Sasami Sasasegawa",
     "Little Busters!",
     "https://cdn.myanimelist.net/images/characters/6/243597.jpg"
    ),(  #393
     "Chisato Nishikigi",                                                               # Lycoris Recoil
     "Lycoris Recoil",
     "https://cdn.myanimelist.net/images/characters/15/497009.jpg"
    ),(  #394
     "Takina Inoue",
     "Lycoris Recoil",
     "https://cdn.myanimelist.net/images/characters/11/484569.jpg"
    ),(  #395
     "Kurumi",
     "Lycoris Recoil",
     "https://cdn.myanimelist.net/images/characters/12/491295.jpg"
    ),(  #396
     "Mizuki Nakahara",
     "Lycoris Recoil",
     "https://cdn.myanimelist.net/images/characters/9/491734.jpg"
    ),(  #397
     "Yuuko Yoshida",                                                                   # Machikado Mazoku
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/8/388684.jpg"
    ),(  #398
     "Momo Chiyoda",
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/12/388685.jpg"
    ),(  #399
     "Lico",
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/6/403342.jpg"
    ),(  #400
     "Mikan Hinatsuki",
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/5/477006.jpg"
    ),(  #401
     "Lilith",
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/14/477314.jpg"
    ),(  #402
     "Ryouko Yoshida",
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/5/477010.jpg"
    ),(  #403
     "Seiko Yoshida",
     "The Demon Girl Next Door",
     "https://cdn.myanimelist.net/images/characters/8/477012.jpg"
    ),(  #404
     "Riko",                                                                            # Made in Abyss
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/15/334267.jpg"
    ),(  #405
     "Nanachi",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/3/471433.jpg"
    ),(  #406
     "Ozen",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/14/358235.jpg"
    ),(  #407
     "Mitty",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/6/340731.jpg"
    ),(  #408
     "Lyza",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/16/338232.jpg"
    ),(  #409
     "Prushka",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/13/471437.jpg"
    ),(  #410
     "Faputa",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/5/471438.jpg"
    ),(  #411
     "Vueko",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/16/471439.jpg"
    ),(  #412
     "Irumyuui",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/5/485489.jpg"
    ),(  #413
     "Maaa",
     "Made in Abyss",
     "https://cdn.myanimelist.net/images/characters/15/452976.jpg"
    ),(  #414
     "Anna Yanami",                                                                     # Makeine: Too Many Losing Heroines
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/7/568413.jpg",
    ),(  #415
     "Chika Komari",
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/5/542557.jpg",
    ),(  #416
     "Lemon Yakishio",
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/13/542559.jpg",
    ),(  #417
     "Kaju Nukumizu",
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/4/552228.jpg",
    ),(  #418
     "Tiara Basori",
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/12/562122.jpg",
    ),(  #419
     "Yumeko Shikiya",
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/16/563587.jpg",
    ),(  #420
     "Karen Himemiya",
     "Makeine: Too Many Losing Heroines!",
     "https://cdn.myanimelist.net/images/characters/16/556131.jpg",
    ),(  #421
     "Aki Adagaki",                                                                         # Masamune-kun's Revenge
     "Masamune-kun's Revenge",
     "https://cdn.myanimelist.net/images/characters/14/324644.jpg",
    ),(  #422
     "Yoshino Koiwai",
     "Masamune-kun's Revenge",
     "https://cdn.myanimelist.net/images/characters/16/315038.jpg",
    ),(  #423
     "Neko Fujinomiya",
     "Masamune-kun's Revenge",
     "https://cdn.myanimelist.net/images/characters/13/323683.jpg",
    ),(  #424
     "Kinue Hayase",
     "Masamune-kun's Revenge",
     "https://cdn.myanimelist.net/images/characters/2/370904.jpg",
    ),(  #425
     "Tae Futaba",
     "Masamune-kun's Revenge",
     "https://cdn.myanimelist.net/images/characters/14/315040.jpg",
    ),(  #426
     "Muriel Besson",
     "Masamune-kun's Revenge",
     "https://cdn.myanimelist.net/images/characters/5/494739.jpg",
    ),(  #427
     "Miko Yotsuya",                                                                        # Mieruko-chan
     "Mieruko-chan",
     "https://cdn.myanimelist.net/images/characters/4/456320.jpg",
    ),(  #428
     "Hana Yurikawa",
     "Mieruko-chan",
     "https://cdn.myanimelist.net/images/characters/14/448308.jpg",
    ),(  #429
     "Yuria Niguredou",
     "Mieruko-chan",
     "https://cdn.myanimelist.net/images/characters/13/448306.jpg",
    ),(  #430
     "Tome Kurata",                                                                         # Mob Psycho 100
     "Mob Psycho 100",
     "https://cdn.myanimelist.net/images/characters/8/306667.jpg",
    ),(  #431
     "Ichi Mezato",
     "Mob Psycho 100",
     "https://cdn.myanimelist.net/images/characters/2/306668.jpg",
    ),(  #432
     "Tsubomi Takane",
     "Mob Psycho 100",
     "https://cdn.myanimelist.net/images/characters/4/306666.jpg",
    ),(  #433
     "Sakurako Shikishima",                                                                 # mono
     "mono",
     "https://cdn.myanimelist.net/images/characters/7/590481.jpg",
    ),(  #434
     "Haruno Akiyama",
     "mono",
     "https://cdn.myanimelist.net/images/characters/2/591871.jpg",
    ),(  #435
     "An Kiriyama",
     "mono",
     "https://cdn.myanimelist.net/images/characters/2/565036.jpg",
    ),(  #436
     "Satsuki Amamiya",
     "mono",
     "https://cdn.myanimelist.net/images/characters/7/589021.jpg",
    ),(  #437
     "Kako Komada",
     "mono",
     "https://cdn.myanimelist.net/images/characters/15/595759.jpg",
    ),(  #438
     "Torayo Kurokuma",
     "mono",
     "https://cdn.myanimelist.net/images/characters/2/592771.jpg",
    ),(  #439
     "Makinohara",
     "mono",
     "https://cdn.myanimelist.net/images/characters/3/589019.jpg",
    ),(  #440
     "Fuuka Inomata",
     "mono",
     "https://cdn.myanimelist.net/images/characters/5/597715.jpg",
    ),(  #441
     "Shinobu Oshino",                                                                      # Monogatari
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/16/234167.jpg",
    ),(  #442
     "Nadeko Sengoku",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/15/405321.jpg",
    ),(  #443
     "Yotsugi Ononoki",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/4/301226.jpg",
    ),(  #444
     "Deathtopia Virtuoso Suicide-Master",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/13/560109.jpg",
    ),(  #445
     "Hitagi Senjougahara",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/8/299586.jpg",
    ),(  #446
     "Mayoi Hachikuji",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/5/222381.jpg",
    ),(  #447
     "Suruga Kanbaru",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/11/222449.jpg",
    ),(  #448
     "Ougi Oshino",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/3/301358.jpg",
    ),(  #449
     "Karen Araragi",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/15/295366.jpg",
    ),(  #450
     "Tsukihi Araragi",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/9/149433.jpg",
    ),(  #451
     "Sodachi Oikura",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/7/300557.jpg",
    ),(  #452
     "Izuko Gaen",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/6/214903.jpg",
    ),(  #453
     "Yozuru Kagenui",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/15/195363.jpg",
    ),(  #454
     "Tsubasa Hanekawa",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/3/288080.jpg",
    ),(  #455
     "Black Hanekawa",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/6/413492.jpg",
    ),(  #456
     "Rouka Numachi",
     "Monogatari",
     "https://cdn.myanimelist.net/images/characters/14/434431.jpg",
    ),(  #457
     "Eris Boreas Greyrat",                                                                   # Mushoku Tensei
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/9/591592.jpg",
    ),(  #458
     "Roxy Migurdia",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/16/552605.jpg",
    ),(  #459
     "Sylphiette",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/10/423669.jpg",
    ),(  #460
     "Ghislaine Dedoldia",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/14/591401.jpg",
    ),(  #461
     "Zenith Greyrat",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/13/591596.jpg",
    ),(  #462
     "Aisha Greyrat",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/16/274691.jpg",
    ),(  #463
     "Norn Greyrat",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/16/593840.jpg",
    ),(  #464
     "Shizuka Nanahoshi",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/6/545654.jpg",
    ),(  #465
     "Elinalise Dragonroad",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/3/460705.jpg",
    ),(  #466
     "Kishirika Kishirisu",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/13/302260.jpg",
    ),(  #467
     "Lilia Greyrat",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/14/593841.jpg",
    ),(  #468
     "Ariel Anemoi Asura",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/15/516104.jpg",
    ),(  #469
     "Rokari Migurdia",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/7/457319.jpg",
    ),(  #470
     "Linia Dedoldia",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/11/518421.jpg",
    ),(  #471
     "Pursena Adoldia",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/15/518422.jpg",
    ),(  #472
     "Juliette",
     "Mushoku Tensei",
     "https://cdn.myanimelist.net/images/characters/2/591589.jpg",
    ),(  #473
     "Hifumi Takimoto",                                                                      # New Game!
     "New Game!",
     "https://media.discordapp.net/attachments/1422999881269645424/1423013456369422376/Hifumi_Takimoto.jpg?"
    ),(  #474
     "Aoba Suzukaze",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/3/311604.jpg",
    ),(  #475
     "Kou Yagami",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/3/311600.jpg",
    ),(  #476
     "Umiko Ahagon",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/9/315670.jpg",
    ),(  #477
     "Nene Sakura",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/11/315674.jpg",
    ),(  #478
     "Yun Iijima",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/12/315672.jpg",
    ),(  #479
     "Hajime Shinoda",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/7/313535.jpg",
    ),(  #480
     "Rin Tooyoma",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/4/313534.jpg",
    ),(  #481
     "Momiji Mochizuki",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/10/339165.jpg",
    ),(  #482
     "Shizuku Hazuki",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/12/315671.jpg",
    ),(  #483
     "Tsubame Narumi",
     "New Game!",
     "https://cdn.myanimelist.net/images/characters/3/330245.jpg",
    ),(  #484
     "Yuuko Aioi",                                                                              # Nichijou
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/15/114020.jpg",
    ),(  #485
     "Hakase Shinonome",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/5/113407.jpg",
    ),(  #486
     "Nano Shinonome",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/11/112682.jpg",
    ),(  #487
     "Mio Naganohara",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/3/116963.jpg",
    ),(  #488
     "Mai Minakami",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/3/114022.jpg",
    ),(  #489
     "Izumi Sakurai",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/10/159693.jpg",
    ),(  #490
     "Misato Tachibana",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/11/159669.jpg",
    ),(  #491
     "Haruna Annaka",
     "Nichijou",
     "https://cdn.myanimelist.net/images/characters/16/114003.jpg",
    ),(  #492
     "Chitoge Kirisaki",                                                                        # Nisekoi
     "Nisekoi",
     "https://cdn.myanimelist.net/images/characters/7/241651.jpg",
    ),(  #493
     "Kosaki Onodera",
     "Nisekoi",
     "https://cdn.myanimelist.net/images/characters/9/241653.jpg",
    ),(  #494
     "Seishirou Tsugumi",
     "Nisekoi",
     "https://cdn.myanimelist.net/images/characters/8/241659.jpg",
    ),(  #495
     "Marika Tachibana",
     "Nisekoi",
     "https://cdn.myanimelist.net/images/characters/15/242521.jpg",
    ),(  #496
     "Haru Onodera",
     "Nisekoi",
     "https://cdn.myanimelist.net/images/characters/11/279030.jpg",
    ),(  #497
     "Ruri Miyamoto",
     "Nisekoi",
     "https://cdn.myanimelist.net/images/characters/9/235033.jpg",
    ),(  #498
     "Shiro",                                                                                 # No Game No Life
     "No Game No Life",
     "https://cdn.myanimelist.net/images/characters/16/246723.jpg",
    ),(  #499
     "Schwi Dola",
     "No Game No Life",
     "https://cdn.myanimelist.net/images/characters/8/336580.jpg",
    ),(  #500
     "Stephanie Dola",
     "No Game No Life",
     "https://cdn.myanimelist.net/images/characters/12/274341.jpg",
    ),(  #501
     "Jibril",
     "No Game No Life",
     "https://cdn.myanimelist.net/images/characters/12/248121.jpg",
    ),(  #502
     "Izuna Hatsuse",
     "No Game No Life",
     "https://cdn.myanimelist.net/images/characters/11/252987.jpg",
    ),(  #503
     "Couronne Dola",
     "No Game No Life",
     "https://cdn.myanimelist.net/images/characters/7/434616.jpg",
    ),(  #504
     "Renge Miyauchi",                                                                      # Non Non Biyori
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/15/288781.jpg",
    ),(  #505
     "Komari Koshigaya",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/3/225067.jpg",
    ),(  #506
     "Hotaru Ichijou",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/15/222839.jpg",
    ),(  #507
     "Natsumi Koshigaya",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/14/222841.jpg",
    ),(  #508
     "Kaede Kagayama",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/7/225829.jpg",
    ),(  #509
     "Hikage Miyauchi",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/2/254703.jpg",
    ),(  #510
     "Kazuho Miyauchi",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/9/254903.jpg",
    ),(  #511
     "Konomi Fujimiya",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/15/230215.jpg",
    ),(  #512
     "Aoi Niizato",
     "Non Non Biyori",
     "https://cdn.myanimelist.net/images/characters/13/428549.jpg",
    ),(  #513
     "Mahiro Oyama",                                                                    # Onimai
     "Onimai",
     "https://cdn.myanimelist.net/images/characters/4/495692.jpg",
    ),(  #514
     "Mihari Oyama",
     "Onimai",
     "https://cdn.myanimelist.net/images/characters/5/495693.jpg",
    ),(  #515
     "Kaede Hozuki",
     "Onimai",
     "https://cdn.myanimelist.net/images/characters/14/495695.jpg",
    ),(  #516
     "Asahi Ouka",
     "Onimai",
     "https://cdn.myanimelist.net/images/characters/4/495697.jpg",
    ),(  #517
     "Momiji Hozuki",
     "Onimai",
     "https://cdn.myanimelist.net/images/characters/10/495696.jpg",
    ),(  #518
     "Miyo Murosaki",
     "Onimai",
     "https://cdn.myanimelist.net/images/characters/5/495694.jpg",
    ),(  #519
     "Holo",                                                                            # Spice and Wolf
     "Spice and Wolf",
     "https://cdn.myanimelist.net/images/characters/12/540685.jpg",
    ),(  #520
     "Nora Arendt",
     "Spice and Wolf",
     "https://cdn.myanimelist.net/images/characters/3/549872.jpg",
    ),(  #521
     "Elsa Schtingheim",
     "Spice and Wolf",
     "https://cdn.myanimelist.net/images/characters/3/562994.jpg",
    ),(  #522
     "Dian Rubens",
     "Spice and Wolf",
     "https://cdn.myanimelist.net/images/characters/10/555751.jpg",
    ),(  #523
     "Ruri Gokou",                                                                      # Oreimo
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/16/343455.jpg",
    ),(  #524
     "Kirino Kousaka",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/8/101419.jpg",
    ),(  #525
     "Ayase Aragaki",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/7/105913.jpg",
    ),(  #526
     "Manami Tamura",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/15/103692.jpg",
    ),(  #527
     "Saori Makishima",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/12/102464.jpg",
    ),(  #528
     "Kanako Kurusu",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/2/103830.jpg",
    ),(  #529
     "Sena Akagi",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/4/208025.jpg",
    ),(  #530
     "Bridget Evans",
     "Oreimo",
     "https://cdn.myanimelist.net/images/characters/6/106194.jpg",
    ),(  #531
     "Ai Fuyuumi",                                                                          # Oreshura
     "Oreshura",
     "https://cdn.myanimelist.net/images/characters/10/191830.jpg"
    ),(  #532
     "Masuzu Natsukawa",
     "Oreshura",
     "https://cdn.myanimelist.net/images/characters/12/191838.jpg",
    ),(  #533
     "Chiwa Harusaki",
     "Oreshura",
     "https://cdn.myanimelist.net/images/characters/5/211941.jpg",
    ),(  #534
     "Himeka Akishino",
     "Oreshura",
     "https://cdn.myanimelist.net/images/characters/6/191832.jpg",
    ),(  #535
     "Mahiru Shiina",                                                            # The Angel Next Door Spoils Me Rotten
     "The Angel Next Door Spoils Me Rotten",
     "https://cdn.myanimelist.net/images/characters/9/468196.jpg",
    ),(  #536
     "Chitose Shirakawa",
     "The Angel Next Door Spoils Me Rotten",
     "https://cdn.myanimelist.net/images/characters/14/468198.jpg",
    ),(  #537
     "Shinoa Hiiragi",                                                                  # Seraph of the End
     "Seraph of the End",
     "https://cdn.myanimelist.net/images/characters/6/285968.jpg",
    ),(  #538
     "Mitsuba Sanguu",
     "Seraph of the End",
     "https://cdn.myanimelist.net/images/characters/6/282911.jpg",
    ),(  #539
     "Krul Tepes",
     "Seraph of the End",
     "https://cdn.myanimelist.net/images/characters/6/460629.jpg",
    ),(  #540
     "Mahiru Hiiragi",
     "Seraph of the End",
     "https://cdn.myanimelist.net/images/characters/2/555408.jpg",
    ),(  #541
     "Chess Belle",
     "Seraph of the End",
     "https://cdn.myanimelist.net/images/characters/14/555410.jpg",
    ),(  #542
     "Isla",                                                                            # Plastic Memories
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/3/517401.jpg",
    ),(  #543
     "Michiru Kinushima",
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/5/280701.jpg",
    ),(  #544
     "Eru Miru",
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/8/280702.jpg",
    ),(  #545
     "Kazuki Kuwanomi",
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/12/280704.jpg",
    ),(  #546
     "Emilia",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/12/524543.jpg",
    ),(  #547
     "Rem",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/10/311627.jpg",
    ),(  #548
     "Ram",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/15/306390.jpg",
    ),(  #549
     "Beatrice",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/2/591066.jpg", #550
    ),(  #551
     "Crusch Karsten",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/5/563863.jpg",
    ),(  #552
     "Satella",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/13/422866.jpg",
    ),(  #553
     "Elsa Granhiert",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/6/302431.jpg",
    ),(  #554
     "Priscilla Barielle",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/14/307861.jpg",
    ),(  #555
     "Felt",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/6/312726.jpg",
    ),(  #556
     "Frederica Baumann",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/3/563873.jpg",
    ),(  #557
     "Theresia van Astrea",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/4/310442.jpg",
    ),(  #558
     "Petra Leyte",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/2/311498.jpg",
    ),(  #559
     "Mimi Pearlbaton",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/9/312730.jpg",
    ),(  #560
     "Anastasia Hoshin",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/4/563866.jpg",
    ),(  #561
     "Echidna",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/4/424981.jpg",
    ),(  #562
     "Ryuuzu Meyer",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/3/411339.jpg",
    ),(  #563
     "Daphne",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/7/419509.jpg",
    ),(  #564
     "Carmilla",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/4/324235.jpg",
    ),(  #565
     "Minerva",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/11/319759.jpg",
    ),(  #566
     "Pandora",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/15/468595.jpg",
    ),(  #567
     "Capella Emerada Lugunica",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/12/560844.jpg",
    ),(  #568
     "Sirius Romanee-Conti",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/13/560846.jpg",
    ),(  #569
     "Rui Arneb",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/7/462992.jpg",
    ),(  #570
     "Liliana Masquerade",
     "Re:Zero",
     "https://cdn.myanimelist.net/images/characters/12/543236.jpg",
    ),(  #571
     "Megumi Katou",
     "Saekano",
     "https://cdn.myanimelist.net/images/characters/15/391806.jpg",
    ),(  #572
     "Utaha Kasumigaoka",
     "Saekano",
     "https://cdn.myanimelist.net/images/characters/10/568217.jpg",
    ),(  #573
     "Eriri Spencer Sawamura",
     "Saekano",
     "https://cdn.myanimelist.net/images/characters/4/325308.jpg",
    ),(  #574
     "Michiru Hyoudou",
     "Saekano",
     "https://cdn.myanimelist.net/images/characters/11/325311.jpg",
    ),(  #575
     "Izumi Hashima",
     "Saekano",
     "https://cdn.myanimelist.net/images/characters/8/325310.jpg",
    ),(  #576
     "Akane Kosaka",
     "Saekano",
     "https://cdn.myanimelist.net/images/characters/12/326876.jpg",
    ),(  #577
     "Mashiro Shiina",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/13/274637.jpg",
    ),(  #578
     "Nanami Aoyama",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/3/198775.jpg",
    ),(  #579
     "Misaki Kamiigusa",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/15/216559.jpg",
    ),(  #580
     "Rita Ainsworth",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/16/324805.jpg",
    ),(  #581
     "Chihiro Sengoku",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/4/188622.jpg",
    ),(  #582
     "Yuuko Kanda",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/5/258027.jpg",
    ),(  #583
     "Maid-chan",
     "The Pet Girl of Sakurasou",
     "https://cdn.myanimelist.net/images/characters/7/324809.jpg",
    ),(  #584
     "Celia Claire",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/6/449418.jpg",
    ),(  #585
     "Aishia",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/5/449422.jpg",
    ),(  #586
     "Miharu Ayase",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/3/449410.jpg",
    ),(  #587
     "Latifa",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/4/553318.jpg",
    ),(  #588
     "Liselotte Cretia",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/2/568002.jpg",
    ),(  #589
     "Flora Beltrum",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/14/424549.jpg",
    ),(  #590
     "Christina Beltrum",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/4/424480.jpg",
    ),(  #591
     "Sara",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/14/566406.jpg",
    ),(  #592
     "Orphia",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/13/424486.jpg",
    ),(  #593
     "Alma",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/9/424477.jpg",
    ),(  #594
     "Dryas",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/10/566408.jpg",
    ),(  #595
     "Ruri",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/5/479224.jpg",
    ),(  #596
     "Sayo",
     "Spirit Chronicles",
     "https://cdn.myanimelist.net/images/characters/8/451103.jpg",
    ),(  #597
     "Mai Sakurajima",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/5/444083.jpg",
    ),(  #598
     "Miniskirt Santa",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/6/599592.jpg",
    ),(  #599
     "Rio Futaba",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/12/567488.jpg",
    ),(  #600
     "Kaede Azusagawa",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/7/366710.jpg",
    ),(  #601
     "Tomoe Koga",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/4/366709.jpg",
    ),(  #602
     "Shouko Makinohara",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/8/366712.jpg",
    ),(  #603
     "Nodoka Toyohama",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/4/598438.jpg",
    ),(  #604
     "Saki Kamisato",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/8/373172.jpg",
    ),(  #605
     "Uzuki Hirokawa",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/4/373171.jpg",
    ),(  #606
     "Miori Mitou",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/9/586422.jpg",
    ),(  #607
     "Ikumi Akagi",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/6/603423.jpg",
    ),(  #608
     "Sara Himeji",
     "Rascal Does Not Dream of Bunny Girl Senpai",
     "https://cdn.myanimelist.net/images/characters/9/586421.jpg",
    ),(  #609
     "Nanako Yukishiro",
     "Senryuu Girl",
     "https://cdn.myanimelist.net/images/characters/14/431332.jpg",
    ),(  #610
     "Kino Yakobe",
     "Senryuu Girl",
     "https://cdn.myanimelist.net/images/characters/2/453268.jpg",
    ),(  #611
     "Amane Katagiri",
     "Senryuu Girl",
     "https://cdn.myanimelist.net/images/characters/11/372259.jpg",
    ),(  #612
     "Tao Hanakai",
     "Senryuu Girl",
     "https://cdn.myanimelist.net/images/characters/10/372258.jpg",
    ),(  #613
     "Koto Ootsuki",
     "Senryuu Girl",
     "https://cdn.myanimelist.net/images/characters/2/372260.jpg",
    ),(  #614
     "Senko",
     "The Helpful Fox Senko-san",
     "https://cdn.myanimelist.net/images/characters/8/417734.jpg",
    ),(  #615
     "Shiro",
     "The Helpful Fox Senko-san",
     "https://cdn.myanimelist.net/images/characters/9/380382.jpg",
    ),(  #616
     "Sora",
     "The Helpful Fox Senko-san",
     "https://cdn.myanimelist.net/images/characters/12/382587.jpg",
    ),(  #617
     "Yasuko Kouenji",
     "The Helpful Fox Senko-san",
     "https://cdn.myanimelist.net/images/characters/4/380384.jpg",
    ),(  #618
     "Kate",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/4/435915.jpg",
    ),(  #619
     "Emilico",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/12/435914.jpg",
    ),(  #620
     "Barbie",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/15/402482.jpg",
    ),(  #621
     "Lou",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/5/435923.jpg",
    ),(  #622
     "Maryrose",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/8/478547.jpg",
    ),(  #623
     "Rosemary",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/4/439865.jpg",
    ),(  #624
     "Louise",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/10/435920.jpg",
    ),(  #625
     "Mia",
     "Shadows House",
     "https://cdn.myanimelist.net/images/characters/2/402487.jpg",
    ),(  #626
     "Shana",
     "Shakugan no Shana",
     "https://cdn.myanimelist.net/images/characters/16/66027.jpg",
    ),(  #627
     "Wilhelmina Carmel",
     "Shakugan no Shana",
     "https://cdn.myanimelist.net/images/characters/9/50367.jpg",
    ),(  #628
     "Kazumi Yoshida",
     "Shakugan no Shana",
     "https://cdn.myanimelist.net/images/characters/10/25397.jpg",
    ),(  #629
     "Hecate",
     "Shakugan no Shana",
     "https://cdn.myanimelist.net/images/characters/12/70681.jpg",
    ),(  #630
     "Margery Daw",
     "Shakugan no Shana",
     "https://cdn.myanimelist.net/images/characters/8/72829.jpg",
    ),(  #631
     "Kaori Miyazono",
     "Your Lie In April",
     "https://cdn.myanimelist.net/images/characters/14/302318.jpg",
    ),(  #632
     "Tsubaki Sawabe",
     "Your Lie In April",
     "https://cdn.myanimelist.net/images/characters/6/353335.jpg",
    ),(  #633
     "Emi Igawa",
     "Your Lie In April",
     "https://cdn.myanimelist.net/images/characters/6/278935.jpg",
    ),(  #634
     "Nagi Aiza",
     "Your Lie In April",
     "https://cdn.myanimelist.net/images/characters/7/276133.jpg",
    ),(  #635
     "Noko Shikanoko",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/4/595489.jpg",
    ),(  #636
     "Meme Bashame",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/13/542122.jpg",
    ),(  #637
     "Torako Koshi",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/6/542120.jpg",
    ),(  #638
     "Anko Koshi",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/16/542121.jpg",
    ),(  #639
     "Neko Nekoyamada",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/8/550601.jpg",
    ),(  #640
     "Kinu Tanukikouji",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/2/550600.jpg",
    ),(  #641
     "Chiharu Tsubameya",
     "My Deer Friend Nokotan",
     "https://cdn.myanimelist.net/images/characters/9/550599.jpg",
    ),(  #642
     "Mikasa Ackerman",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/9/215563.jpg",
    ),(  #643
     "Hange Zoe",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/15/208637.jpg",
    ),(  #644
     "Sasha Blouse",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/6/251937.jpg",
    ),(  #645
     "Annie Leonhart",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/9/206357.jpg",
    ),(  #646
     "Krista Lenz",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/16/216967.jpg",
    ),(  #647
     "Ymir",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/9/226171.jpg",
    ),(  #648
     "Petra Ral",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/8/217555.jpg",
    ),(  #649
     "Hitch Dreyse",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/10/220845.jpg",
    ),(  #650
     "Pieck Finger",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/4/425880.jpg",
    ),(  #651
     "Gabi Braun",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/4/431018.jpg",
    ),(  #652
     "Yelena",
     "Attack on Titan",
     "https://cdn.myanimelist.net/images/characters/13/433243.jpg",
    ),(  #653
     "Saki Watanabe",
     "Shinsekai Yori",
     "https://cdn.myanimelist.net/images/characters/11/183115.jpg",
    ),(  #654
     "Maria Akizuki",
     "Shinsekai Yori",
     "https://cdn.myanimelist.net/images/characters/4/183067.jpg",
    ),(  #655
     "Tomiko Asahina",
     "Shinsekai Yori",
     "https://cdn.myanimelist.net/images/characters/13/190212.jpg",
    ),(  #656
     "Akki",
     "Shinsekai Yori",
     "https://cdn.myanimelist.net/images/characters/13/279762.jpg",
    ),(  #657
     "Kukuru Misakino",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/2/443039.jpg",
    ),(  #658
     "Fuuka Miyazawa",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/11/443046.jpg",
    ),(  #659
     "Karin Kudaka",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/7/443048.jpg",
    ),(  #660
     "Kaoru Shimabukuro",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/16/454865.jpg",
    ),(  #661
     "Chiyu Haebaru",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/13/472578.jpg",
    ),(  #662
     "Tsukimi Teruya",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/16/443049.jpg",
    ),(  #663
     "Akari Maeda",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/11/454864.jpg",
    ),(  #664
     "Marina Yonekura",
     "The Aquatope on White Sand",
     "https://cdn.myanimelist.net/images/characters/6/472789.jpg",
    ),(  #665
     "Ouka Shiunji",
     "The Shiunji Family Children",
     "https://cdn.myanimelist.net/images/characters/6/558436.jpg",
    ),(  #666
     "Seiha Shiunji",
     "The Shiunji Family Children",
     "https://cdn.myanimelist.net/images/characters/9/567630.jpg",
    ),(  #667
     "Banri Shiunji",
     "The Shiunji Family Children",
     "https://cdn.myanimelist.net/images/characters/5/567556.jpg",
    ),(  #668
     "Kotono Shiunji",
     "The Shiunji Family Children",
     "https://cdn.myanimelist.net/images/characters/2/568350.jpg",
    ),(  #669
     "Minami Shiunji",
     "The Shiunji Family Children",
     "https://cdn.myanimelist.net/images/characters/5/568083.jpg",
    ),(  #670
     "Chito",
     "Girls' Last Tour",
     "https://cdn.myanimelist.net/images/characters/5/341027.jpg",
    ),(  #671
     "Yuuri",
     "Girls' Last Tour",
     "https://cdn.myanimelist.net/images/characters/7/341028.jpg",
    ),(  #672
     "Ishii",
     "Girls' Last Tour",
     "https://cdn.myanimelist.net/images/characters/11/344063.jpg",
    ),(  #673
     "Chtholly Nota Seniorious",
     "WorldEnd",
     "https://cdn.myanimelist.net/images/characters/12/327424.jpg",
    ),(  #674
     "Nephren Ruq Insania",
     "WorldEnd",
     "https://cdn.myanimelist.net/images/characters/13/332794.jpg",
    ),(  #675
     "Ithea Myse Valgulious",
     "WorldEnd",
     "https://cdn.myanimelist.net/images/characters/14/327408.jpg",
    ),(  #676
     "Rhantolk Ytri Historia",
     "WorldEnd",
     "https://cdn.myanimelist.net/images/characters/13/327410.jpg",
    ),(  #677
     "Elq Hrqstn",
     "WorldEnd",
     "https://cdn.myanimelist.net/images/characters/7/329825.jpg",
    ),(  #678
     "Nygglatho",
     "WorldEnd",
     "https://cdn.myanimelist.net/images/characters/2/327417.jpg",
    ),(  #679
     "Akira Shinonome",
     "Train to the End of the World",
     "https://cdn.myanimelist.net/images/characters/6/518133.jpg",
    ),(  #680
     "Reimi Kuga",
     "Train to the End of the World",
     "https://cdn.myanimelist.net/images/characters/13/518134.jpg",
    ),(  #681
     "Shizuru Chikura",
     "Train to the End of the World",
     "https://cdn.myanimelist.net/images/characters/16/516825.jpg",
    ),(  #682
     "Nadeshiko Hoshi",
     "Train to the End of the World",
     "https://cdn.myanimelist.net/images/characters/9/518135.jpg",
    ),(  #683
     "Mito Kuroki",
     "Train to the End of the World",
     "https://cdn.myanimelist.net/images/characters/9/548435.jpg",
    ),(  #684
     "Youka Nakatomi",
     "Train to the End of the World",
     "https://cdn.myanimelist.net/images/characters/5/543768.jpg",
    ),(  #685
     "Mitsumi Iwakura",
     "Skip and Loafer",
     "https://cdn.myanimelist.net/images/characters/16/509649.jpg",
    ),(  #686
     "Yuzuki Murashige",
     "Skip and Loafer",
     "https://cdn.myanimelist.net/images/characters/6/509651.jpg",
    ),(  #687
     "Mika Egashira",
     "Skip and Loafer",
     "https://cdn.myanimelist.net/images/characters/3/573523.jpg",
    ),(  #688
     "Makoto Kurume",
     "Skip and Loafer",
     "https://cdn.myanimelist.net/images/characters/11/509650.jpg",
    ),(  #689
     "Azusa",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/10/440267.jpg",
    ),(  #690
     "Laika",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/6/440268.jpg",
    ),(  #691
     "Falfa",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/13/440271.jpg",
    ),(  #692
     "Halkara",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/15/440269.jpg",
    ),(  #693
     "Shalsha",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/16/440270.jpg",
    ),(  #694
     "Beelzebub",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/3/440272.jpg",
    ),(  #695
     "Flatorte",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/13/440273.jpg",
    ),(  #696
     "Pecora",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/4/440275.jpg",
    ),(  #697
     "Rosalie",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/9/440274.jpg",
    ),(  #698
     "Vania",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/3/588954.jpg",
    ),(  #699
     "Fatla",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/6/588953.jpg",
    ),(  #700
     "Kuku",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/16/597017.jpg",
    ),(  #701
     "Sandra",
     "I've Been Killing Slimes for 300 Years and Maxed Out My Level",
     "https://cdn.myanimelist.net/images/characters/13/574768.jpg",
    ),(  #702
     "Hiyori Minagi",
     "Slow Loop",
     "https://cdn.myanimelist.net/images/characters/16/459274.jpg",
    ),(  #703
     "Koharu Minagi",
     "Slow Loop",
     "https://cdn.myanimelist.net/images/characters/6/459273.jpg",
    ),(  #704
     "Koi Yoshinaga",
     "Slow Loop",
     "https://cdn.myanimelist.net/images/characters/6/459278.jpg",
    ),(  #705
     "Ichika Fukumoto",
     "Slow Loop",
     "https://cdn.myanimelist.net/images/characters/4/459276.jpg",
    ),(  #706
     "Aiko Ninomiya",
     "Slow Loop",
     "https://cdn.myanimelist.net/images/characters/15/459277.jpg",
    ),(  #707
     "Futaba Fukumoto",
     "Slow Loop",
     "https://cdn.myanimelist.net/images/characters/11/459275.jpg",
    ),(  #708
     "Tamate Momochi",
     "Slow Start",
     "https://cdn.myanimelist.net/images/characters/3/352730.jpg",
    ),(  #709
     "Kamuri Sengoku",
     "Slow Start",
     "https://cdn.myanimelist.net/images/characters/12/336052.jpg",
    ),(  #710
     "Hana Ichinose",
     "Slow Start",
     "https://cdn.myanimelist.net/images/characters/3/336049.jpg",
    ),(  #711
     "Eiko Tokura",
     "Slow Start",
     "https://cdn.myanimelist.net/images/characters/16/336051.jpg",
    ),(  #712
     "Hiroe Hannen",
     "Slow Start",
     "https://cdn.myanimelist.net/images/characters/6/344320.jpg",
    ),(  #713
     "Shion Kyouzuka",
     "Slow Start",
     "https://cdn.myanimelist.net/images/characters/10/344319.jpg",
    ),(  #714
     "Marin Kitagawa",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/16/599495.jpg",
    ),(  #715
     "Sajuna Inui",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/2/598040.jpg",
    ),(  #716
     "Shinju Inui",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/6/598042.jpg",
    ),(  #717
     "Nowa Sugaya",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/11/464449.jpg",
    ),(  #718
     "Akira Ogata",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/11/603196.jpg",
    ),(  #719
     "Seira Kasai",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/12/601778.jpg",
    ),(  #720
     "Rune Yamauchi",
     "My Dress-Up Darling",
     "https://cdn.myanimelist.net/images/characters/7/468457.jpg",
    ),(  #721
     "Shirase Kobuchizawa",
     "A Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/14/363064.jpg",
    ),(  #722
     "Hinata Miyake",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/12/365996.jpg",
    ),(  #723
     "Mari Tamaki",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/14/358826.jpg",
    ),(  #724
     "Yuzuki Shiraishi",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/11/366095.jpg",
    ),(  #725
     "Gin Toudou",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/4/345983.jpg",
    ),(  #726
     "Yumiko Samejima",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/16/345981.jpg",
    ),(  #727
     "Megumi Takahashi",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/4/345980.jpg",
    ),(  #728
     "Kanae Maekawa",
     "Place Further Than The Universe",
     "https://cdn.myanimelist.net/images/characters/13/345982.jpg",
    ),(  #729
     "Frieren",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/7/525105.jpg",
    ),(  #730
     "Fern",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/4/561357.jpg"
    ),(  #731
     "Ubel",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/6/541934.jpg",
    ),(  #732
     "Flamme",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/10/528177.jpg",
    ),(  #733
     "Serie",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/14/537346.jpg",
    ),(  #734
     "Methode",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/14/538692.jpg",
    ),(  #735
     "Sense",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/14/538685.jpg",
    ),(  #736
     "Aura",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/8/566310.jpg",
    ),(  #737
     "Linie",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/13/524721.jpg",
    ),(  #738
     "Laufen",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/2/538687.jpg",
    ),(  #739
     "Lawine",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/10/537013.jpg",
    ),(  #740
     "Kanne",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/13/543071.jpg",
    ),(  #741
     "Ehre",
     "Frieren: Beyond Journey's End",
     "https://cdn.myanimelist.net/images/characters/12/531661.jpg",
    ),(  #742
     "Anya Forger",
     "Spy x Family",
     "https://cdn.myanimelist.net/images/characters/4/469910.jpg",
    ),(  #743
     "Yor Forger",
     "Spy x Family",
     "https://cdn.myanimelist.net/images/characters/13/473283.jpg",
    ),(  #744
     "Becky Blackbell",
     "Spy x Family",
     "https://cdn.myanimelist.net/images/characters/3/528426.jpg",
    ),(  #745
     "Sylvia Sherwood",
     "Spy x Family",
     "https://cdn.myanimelist.net/images/characters/3/467192.jpg",
    ),(  #746
     "Fiona Frost",
     "Spy x Family",
     "https://cdn.myanimelist.net/images/characters/4/494104.jpg",
    ),(  #747
     "Kurisu Makise",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/12/492885.jpg",
    ),(  #748
     "Mayuri Shiina",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/10/113698.jpg",
    ),(  #749
     "Suzuha Amane",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/3/148223.jpg",
    ),(  #750
     "Rumiho Akiha",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/2/142621.jpg",
    ),(  #751
     "Nae Tennouji",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/16/353319.jpg",
    ),(  #752
     "Moeka Kiryuu",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/12/275310.jpg",
    ),(  #753
     "Maho Hiyajou",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/14/345914.jpg",
    ),(  #754
     "Kagari Shiina",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/16/353317.jpg",
    ),(  #755
     "Yuki Amane",
     "Steins;Gate",
     "https://cdn.myanimelist.net/images/characters/16/362836.jpg",
    ),(  #756
     "Ai Mie",
     "The Girl I Like Forgot Her Glasses",
     "https://cdn.myanimelist.net/images/characters/9/519539.jpg",
    ),(  #757
     "Haruhi Suzumiya",
     "The Melancholy of Haruhi Suzumiya",
     "https://cdn.myanimelist.net/images/characters/4/318548.jpg",
    ),(  #758
     "Yuki Nagato",
     "The Melancholy of Haruhi Suzumiya",
     "https://cdn.myanimelist.net/images/characters/11/319309.jpg",
    ),(  #759
     "Mikuru Asahina",
     "The Melancholy of Haruhi Suzumiya",
     "https://cdn.myanimelist.net/images/characters/10/75526.jpg",
    ),(  #760
     "Tsuruya",
     "The Melancholy of Haruhi Suzumiya",
     "https://cdn.myanimelist.net/images/characters/16/73654.jpg",
    ),(  #761
     "Ryouko Asakura",
     "The Melancholy of Haruhi Suzumiya",
     "https://cdn.myanimelist.net/images/characters/7/89053.jpg",
    ),(  #762
     "Kyon's Sister",
     "The Melancholy of Haruhi Suzumiya",
     "https://cdn.myanimelist.net/images/characters/4/89052.jpg",
    ),(  #763
     "Shizuka Kuze",
     "Takopi's Orignal Sin",
     "https://cdn.myanimelist.net/images/characters/12/573206.jpg",
    ),(  #764
     "Marina Kirarazaka",
     "Takopi's Original Sin",
     "https://cdn.myanimelist.net/images/characters/10/584540.jpg",
    ),(  #765
     "Hina Amano",
     "Weathering With You",
     "https://cdn.myanimelist.net/images/characters/9/408525.jpg",
    ),(  #766
     "Natsumi Suga",
     "Weathering With You",
     "https://cdn.myanimelist.net/images/characters/12/484549.jpg",
    ),(  #767
     "Alya Kujou",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/5/536830.jpg",
    ),(  #768
     "Yuki Suou",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/12/559107.jpg",
    ),(  #769
     "Masha Kujou",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/13/536833.jpg",
    ),(  #770
     "Ayano Kimishima",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/6/536829.jpg",
    ),(  #771
     "Nonoa Miyamae",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/10/561182.jpg",
    ),(  #772
     "Chisaki Sarashina",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/12/558852.jpg",
    ),(  #773
     "Sayaka Taniyama",
     "Alya Sometimes Hides Her Feelings in Russian",
     "https://cdn.myanimelist.net/images/characters/9/561184.jpg",
    ),(  #774
     "Sophie Twilight",
     "Ms. Vampire who lives in my neighborhood.",
     "https://cdn.myanimelist.net/images/characters/14/363481.jpg",
    ),(  #775
     "Elly",
     "Ms. Vampire who lives in my neighborhood.",
     "https://cdn.myanimelist.net/images/characters/15/363478.jpg",
    ),(  #776
     "Akari Amano",
     "Ms. Vampire who lives in my neighborhood.",
     "https://cdn.myanimelist.net/images/characters/11/363476.jpg",
    ),(  #777
     "Hinata Natsuki",
     "Ms. Vampire who lives in my neighborhood.",
     "https://cdn.myanimelist.net/images/characters/5/363477.jpg",
    ),(  #778
     "Yuu Aoki",
     "Ms. Vampire who lives in my neighborhood.",
     "https://cdn.myanimelist.net/images/characters/13/363480.jpg",
    ),(  #779
     "Sakuya Kurai",
     "Ms. Vampire who lives in my neighborhood.",
     "https://cdn.myanimelist.net/images/characters/3/363479.jpg",
    ),(  #780
     "Tsukasa Yuzaki",
     "Tonikawa",
     "https://cdn.myanimelist.net/images/characters/3/445451.jpg",
    ),(  #781
     "Kaname Arisugawa",
     "Tonikawa",
     "https://cdn.myanimelist.net/images/characters/10/418286.jpg",
    ),(  #782
     "Aya Arisugawa",
     "Tonikawa",
     "https://cdn.myanimelist.net/images/characters/7/418284.jpg",
    ),(  #783
     "Charlotte",
     "Tonikawa",
     "https://cdn.myanimelist.net/images/characters/7/453511.jpg",
    ),(  #784
     "Chitose Kaginoji",
     "Tonikawa",
     "https://cdn.myanimelist.net/images/characters/6/418287.jpg",
    ),(  #785
     "Aurora",
     "Tonikawa",
     "https://cdn.myanimelist.net/images/characters/5/428785.jpg",
    ),(  #786
     "Taiga Aisaka",
     "Toradora!",
     "https://cdn.myanimelist.net/images/characters/11/514086.jpg",
    ),(  #787
     "Minori Kushieda",
     "Toradora!",
     "https://cdn.myanimelist.net/images/characters/11/514090.jpg",
    ),(  #788
     "Ami Kawashima",
     "Toradora!",
     "https://cdn.myanimelist.net/images/characters/7/46814.jpg",
    ),(  #789
     "Yasuko Takasu",
     "Toradora!",
     "https://cdn.myanimelist.net/images/characters/15/105456.jpg",
    ),(  #790
     "Elfaria Albis Serfort",
     "Wistoria: Wand and Sword",
     "https://cdn.myanimelist.net/images/characters/2/563704.jpg",
    ),(  #791
     "Colette Loire",
     "Wistoria: Wand and Sword",
     "https://cdn.myanimelist.net/images/characters/11/539536.jpg",
    ),(  #792
     "Lihanna Owenzaus",
     "Wistoria: Wand and Sword",
     "https://cdn.myanimelist.net/images/characters/9/543246.jpg",
    ),(  #793
     "Vivy",
     "Vivy: Flourite Eye's Song",
     "https://cdn.myanimelist.net/images/characters/5/437608.jpg",
    ),(  #794
     "Estella",
     "Vivy: Flourite Eye's Song",
     "https://cdn.myanimelist.net/images/characters/10/437606.jpg",
    ),(  #795
     "Ophelia",
     "Vivy: Flourite Eye's Song",
     "https://cdn.myanimelist.net/images/characters/6/437607.jpg",
    ),(  #796
     "Tomoko Kuroki",
     "WataMote",
     "https://cdn.myanimelist.net/images/characters/15/212635.jpg",
    ),(  #797
     "Yuu Naruse",
     "WataMote",
     "https://cdn.myanimelist.net/images/characters/12/220875.jpg",
    ),(  #798
     "Ai Ohto",
     "Wonder Egg Priority",
     "https://cdn.myanimelist.net/images/characters/10/431621.jpg",
    ),(  #799
     "Rika Kawai",
     "Wonder Egg Priority",
     "https://cdn.myanimelist.net/images/characters/5/441004.jpg",
    ),(  #800
     "Momoe Sawaki",
     "Wonder Egg Priority",
     "https://cdn.myanimelist.net/images/characters/16/443975.jpg",
    ),(  #801
     "Neiru Aonuma",
     "Wonder Egg Priority",
     "https://cdn.myanimelist.net/images/characters/15/443976.jpg",
    ),(  #802
     "Frill",
     "Wonder Egg Priority",
     "https://cdn.myanimelist.net/images/characters/10/437383.jpg",
    ),(  #803
     "Koito Nagase",
     "Wonder Egg Priority",
     "https://cdn.myanimelist.net/images/characters/12/430337.jpg",
    ),(  #804
     "Yukino Yukinoshita",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/16/309714.jpg",
    ),(  #805
     "Yui Yuigahama",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/2/332632.jpg",
    ),(  #806
     "Iroha Isshiki",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/8/320273.jpg",
    ),(  #807
     "Shizuka Hiratsuka",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/2/568221.jpg",
    ),(  #808
     "Komachi Hikigaya",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/16/280870.jpg",
    ),(  #809
     "Saki Kawasaki",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/11/309088.jpg",
    ),(  #810
     "Haruno Yukinoshita",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/5/309077.jpg",
    ),(  #811
     "Mother Yuigahama",
     "My Teen Romantic Comedu SNAFU",
     "https://cdn.myanimelist.net/images/characters/2/285624.jpg",
    ),(  #812
     "Emma",
     "The Promised Neverland",
     "https://cdn.myanimelist.net/images/characters/13/373577.jpg",
    ),(  #813
     "Isabella",
     "The Promised Neverland",
     "https://cdn.myanimelist.net/images/characters/5/462007.jpg",
    ),(  #814
     "Sister Krone",
     "The Promised Neverland",
     "https://cdn.myanimelist.net/images/characters/14/379977.jpg",
    ),(  #815
     "Gilda",
     "The Promised Neverland",
     "https://cdn.myanimelist.net/images/characters/8/360047.jpg",
    ),(  #816
     "Aoi Yukimura",
     "Yama no Susume",
     "https://cdn.myanimelist.net/images/characters/16/514087.jpg",
    ),(  #817
     "Kokona Aoba",
     "Yama no Susume",
     "https://cdn.myanimelist.net/images/characters/4/514344.jpg",
    ),(  #818
     "Hinata Kuraue",
     "Yama no Susume",
     "https://cdn.myanimelist.net/images/characters/10/514340.jpg",
    ),(  #819
     "Kaede Saitou",
     "Yama no Susume",
     "https://cdn.myanimelist.net/images/characters/7/514342.jpg",
    ),(  #820
     "Honoka Kurosaki",
     "Yama no Susume",
     "https://cdn.myanimelist.net/images/characters/3/514346.jpg",
    ),(  #821
     "Hikari Onozuka",
     "Yama no Susume",
     "https://cdn.myanimelist.net/images/characters/15/331848.jpg",
    ),(  #822
     "Akane Kinoshita",
     "My Love Story With Yamada-kun at Lv999",
     "https://cdn.myanimelist.net/images/characters/2/511460.jpg",
    ),(  #823
     "Runa Sasaki",
     "My Love Story With Yamada-kun at Lv999",
     "https://cdn.myanimelist.net/images/characters/2/510117.jpg",
    ),(  #824
     "Yukari Tsubaki",
     "My Love Story With Yamada-kun at Lv999",
     "https://cdn.myanimelist.net/images/characters/4/569532.jpg",
    ),(  #825
     "Momoko Maeda",
     "My Love Story With Yamada-kun at Lv999",
     "https://cdn.myanimelist.net/images/characters/9/505809.jpg",
    ),(  #826
     "Kano Yamanouchi",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/13/537588.jpg",
    ),(  #827
     "Kiui Watase",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/13/537587.jpg",
    ),(  #828
     "Mahiru Kouzuki",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/8/537585.jpg",
    ),(  #829
     "Kim Anouk Mei Takanashi",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/8/537586.jpg",
    ),(  #830
     "Shizue Baba",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/11/537593.jpg",
    ),(  #831
     "Koharu",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/2/544514.jpg",
    ),(  #832
     "Mero Setou",
     "Jellyfish Can't Swim in the Night",
     "https://cdn.myanimelist.net/images/characters/14/537591.jpg",
    ),(  #833
     "Rin Shima",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/14/353089.jpg",
    ),(  #834
     "Nadeshiko Kagamihara",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/2/366169.jpg",
    ),(  #835
     "Aoi Inuyama",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/11/366111.jpg",
    ),(  #836
     "Chiaki Oogaki",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/13/366112.jpg",
    ),(  #837
     "Ena Saitou",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/12/337015.jpg",
    ),(  #838
     "Ayano Toki",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/14/458550.jpg",
    ),(  #839
     "Sakura Kagamihara",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/3/350652.jpg",
    ),(  #840
     "Minami Toba",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/13/543900.jpg",
    ),(  #841
     "Akari Inuyama",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/15/543899.jpg",
    ),(  #842
     "Saki Shima",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/15/350651.jpg",
    ),(  #843
     "Ema Mizunami",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/7/543839.jpg",
    ),(  #844
     "Mei Nakatsugawa",
     "Yuru Camp",
     "https://cdn.myanimelist.net/images/characters/16/543790.jpg",
    ),(  #845
     "Kanade",
     "Beast Tamer",
     "https://cdn.myanimelist.net/images/characters/15/476772.jpg",
    ),(  #846
     "Tania",
     "Beast Tamer",
     "https://cdn.myanimelist.net/images/characters/8/476767.jpg",
    ),(  #847
     "Nina",
     "Beast Tamer",
     "https://cdn.myanimelist.net/images/characters/6/487341.jpg",
    ),(  #848
     "Sora",
     "Beast Tamer",
     "https://cdn.myanimelist.net/images/characters/4/492821.jpg",
    ),(  #849
     "Runa",
     "Beast Tamer",
     "https://cdn.myanimelist.net/images/characters/11/492822.jpg",
    ),(  #850
     "Tina Holly",
     "Beast Tamer",
     "https://cdn.myanimelist.net/images/characters/7/497559.jpg",
    ),(  #851
     "Saki Nikaidou",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/3/590629.jpg",
    ),(  #852
     "Tae Yamada",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/11/590630.jpg",
    ),(  #853
     "Junko Konno",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/14/590631.jpg",
    ),(  #854
     "Sakura Minamoto",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/4/563295.jpg",
    ),(  #855
     "Ai Mizuno",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/15/590633.jpg",
    ),(  #856
     "Lily Hoshikawa",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/7/590634.jpg",
    ),(  #857
     "Yuugiri",
     "Zombie Land Saga",
     "https://cdn.myanimelist.net/images/characters/5/590635.jpg",
    ),(  #858
     "Kana Arima",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/15/511687.jpg",
    ),(  #859
     "Akane Kurokawa",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/15/557228.jpg",
    ),(  #860
     "Ai Hoshino",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/15/502486.jpg",
    ),(  #861
     "Ruby Hoshino",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/5/496454.jpg",
    ),(  #862
     "Mem-Cho",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/8/507015.jpg",
    ),(  #863
     "Miyako Saitou",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/11/511321.jpg",
    ),(  #864
     "Abiko Samejima",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/12/555875.jpg",
    ),(  #865
     "Minami Kotobuki",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/15/510752.jpg",
    ),(  #866
     "Frill Shiranui",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/6/510750.jpg",
    ),(  #867
     "Tsukuyomi",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/7/558252.jpg",
    ),(  #868
     "Yuki Sumi",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/4/512399.jpg",
    ),(  #869
     "Yoriko Kichijouji",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/7/510753.jpg",
    ),(  #870
     "Mei Adashino",
     "Oshi no Ko",
     "https://cdn.myanimelist.net/images/characters/9/555135.jpg",
    ),(  #871
     "Shizuku Murasaki",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/6/373727.jpg",
    ),(  #872
     "Biscuit Krueger",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/5/194667.jpg",
    ),(  #873
     "Machi Komachine",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/10/175943.jpg",
    ),(  #874
     "Pakunoda",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/11/193011.jpg",
    ),(  #875
     "Canary",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/15/160577.jpg",
    ),(  #876
     "Ponzu",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/13/155619.jpg",
    ),(  #877
     "Menchi",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/10/140833.jpg",
    ),(  #878
     "Neon Nostrade",
     "Hunter x Hunter",
     "https://cdn.myanimelist.net/images/characters/16/185665.jpg",
    ),(  #879
     "Delta",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/15/563720.jpg",
    ),(  #880
     "Alpha",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/16/491824.jpg",
    ),(  #881
     "Beta",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/12/483022.jpg",
    ),(  #882
     "Alexia Midgar",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/4/571548.jpg",
    ),(  #883
     "Claire Kagenou",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/9/486844.jpg",
    ),(  #884
     "Epsilon",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/15/483024.jpg",
    ),(  #885
     "Gamma",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/5/483023.jpg",
    ),(  #886
     "Aurora",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/14/563764.jpg",
    ),(  #887
     "Zeta",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/10/483019.jpg",
    ),(  #888
     "Eta",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/15/483018.jpg",
    ),(  #889
     "Rose Oriana",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/14/486846.jpg",
    ),(  #890
     "Beatrix",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/10/563776.jpg",
    ),(  #891
     "Nu",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/7/563762.jpg",
    ),(  #892
     "Sherry Barnett",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/10/563800.jpg",
    ),(  #893
     "Victoria",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/3/521546.jpg",
    ),(  #894
     "Iris Midgar",
     "The Eminence in Shadow",
     "https://cdn.myanimelist.net/images/characters/6/461067.jpg",
    ),(  #895
     "Aries Spring",
     "Astra Lost in Space",
     "https://cdn.myanimelist.net/images/characters/6/377934.jpg",
    ),(  #896
     "Quitterie Raffaeli",
     "Astra Lost in Space",
     "https://cdn.myanimelist.net/images/characters/4/390696.jpg",
    ),(  #897
     "Yunhua Lu",
     "Astra Lost in Space",
     "https://cdn.myanimelist.net/images/characters/8/384726.jpg",
    ),(  #898
     "Funicia Raffaeli",
     "Astra Lost in Space",
     "https://cdn.myanimelist.net/images/characters/7/390693.jpg",
    ),(  #899
     "Seira",
     "Astra Lost in Space",
     "https://cdn.myanimelist.net/images/characters/4/389532.jpg",
    ),(  #900
     "Polina Livinskaya",
     "Astra Lost in Space",
     "https://cdn.myanimelist.net/images/characters/3/386621.jpg",
    ),(  #901
     "Suletta Mercury",
     "Mobile Suit Gundam: The Witch From Mercury",
     "https://cdn.myanimelist.net/images/characters/13/495848.jpg",
    ),(  #902
     "Miorine Rembran",
     "Mobile Suit Gundam: The Witch From Mercury",
     "https://cdn.myanimelist.net/images/characters/9/495846.jpg",
    ),(  #903
     "Chuatury Panlunch",
     "Mobile Suit Gundam: The Witch From Mercury",
     "https://cdn.myanimelist.net/images/characters/11/487017.jpg",
    ),(  #904
     "Prospera Mercury",
     "Mobile Suit Gundam: The Witch From Mercury",
     "https://cdn.myanimelist.net/images/characters/8/490082.jpg",
    ),(  #905
     "Victorique de Blois",
     "Gosick",
     "https://cdn.myanimelist.net/images/characters/5/108860.jpg",
    ),(  #906
     "Cecile Lafitte",
     "Gosick",
     "https://cdn.myanimelist.net/images/characters/6/109028.jpg",
    ),(  #907
     "Avril Bradley",
     "Gosick",
     "https://cdn.myanimelist.net/images/characters/2/122813.jpg",
    ),(  #908
     "Chika Suzugamori",
     "Zatsu Tabi: That's Journey",
     "https://cdn.myanimelist.net/images/characters/6/563018.jpg",
    ),(  #909
     "Koyomi Hasunuma",
     "Zatsu Tabi: That's Journey",
     "https://cdn.myanimelist.net/images/characters/8/589438.jpg",
    ),(  #910
     "Yui Unoki",
     "Zatsu Tabi: That's Journey",
     "https://cdn.myanimelist.net/images/characters/4/563000.jpg",
    ),(  #911
     "Fuyune Koujiya",
     "Zatsu Tabi: That's Journey",
     "https://cdn.myanimelist.net/images/characters/11/573362.jpg",
    ),(  #912
     "Riri Tenkuubashi",
     "Zatsu Tabi: That's Journey",
     "https://cdn.myanimelist.net/images/characters/15/573361.jpg",
    ),(  #913
     "Asuna Yuuki",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/15/262053.jpg",
    ),(  #914
     "Leafa",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/5/254605.jpg",
    ),(  #915
     "Yui",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/15/264165.jpg",
    ),(  #916
     "Keiko Ayano",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/10/185423.jpg",
    ),(  #917
     "Rika Shinozaki",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/8/177115.jpg",
    ),(  #918
     "Sachi",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/7/264145.jpg",
    ),(
     "Toukai Teiou",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/574441.jpg",
    ),(
     "Oguri Cap",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/595961.jpg",
    ),(
     "Gold Ship",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/574452.jpg",
    ),(
     "Special Week",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/2/355244.jpg",
    ),(
     "Mejiro McQueen",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/2/352166.jpg",
    ),(
     "Silence Shizuka",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/16/574439.jpg",
    ),(
     "Haru Urara",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/5/574420.jpg",
    ),(
     "T.M. Opera O",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/574425.jpg",
    ),(
     "Nice Nature",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/16/574458.jpg",
    ),(
     "Daiwa Scarlet",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/7/574416.jpg",
    ),(
     "Symboli Rudolf",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/574440.jpg",
    ),(
     "Tamamo Cross",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/15/573645.jpg",
    ),(
     "El Condor Pasa",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/574468.jpg",
    ),(
     "Seiun Sky",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/16/574428.jpg",
    ),(
     "Maruzensky",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/16/574473.jpg",
    ),(
     "Vodka",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/2/574465.jpg",
    ),(
     "Super Creek",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/6/574482.jpg",
    ),(
     "Grass Wonder",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/7/574470.jpg",
    ),(
     "Meishou Dotou",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/15/574423.jpg",
    ),(
     "King Halo",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/12/574421.jpg",
    ),(
     "Biwa Hayahide",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/5/574431.jpg",
    ),(
     "Narita Brian",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/574437.jpg",
    ),(
     "Taiki Shuttle",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/3/574484.jpg",
    ),(
     "Hishi Amazon",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/3/574478.jpg",
    ),(
     "Matikanefukukitaru",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/8/574455.jpg",
    ),(
     "Air Groove",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/574446.jpg",
    ),(
     "Fuji Kiseki",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/9/574884.jpg",
    ),(
     "Eishin Flash",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/5/574477.jpg",
    ),(
     "Narita Taishin",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/14/574432.jpg",
    ),(
     "Rice Shower",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/574424.jpg",
    ),(
     "Kitasan Black",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/574443.jpg",
    ),(
     "Twin Turbo",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/11/574462.jpg",
    ),(
     "Matikane Tannhauser",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/7/574454.jpg",
    ),(
     "Satono Diamond",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/574445.jpg",
    ),(
     "Mayano Top Gun",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/13/574435.jpg",
    ),(
     "Mihono Bourbon",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/5/574436.jpg",
    ),(
     "Daitaku Helios",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/2/574450.jpg",
    ),(
     "Sakura Bakushin-O",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/13/574438.jpg",
    ),(
     "Ikuno Dictus",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/16/574453.jpg",
    ),(
     "Gold City",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/574419.jpg",
    ),(
     "Mejiro Palmer",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/574419.jpg",
    ),(
     "Misato Akasaka",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/11/588042.jpg",
    ),(
     "Cheval Grand",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/14/574448.jpg",
    ),(
     "Vivlos",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/14/574464.jpg",
    ),(
     "Duramente",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/2/574451.jpg",
    ),(
     "Copano Rickey",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/9/574449.jpg",
    ),(
     "Verxina",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/8/574463.jpg",
    ),(
     "Satono Crown",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/11/588429.jpg",
    ),(
     "Fujimasa March",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/582042.jpg",
    ),(
     "Belno Light",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/8/582041.jpg",
    ),(
     "Sirius Symboli",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/5/574475.jpg",
    ),(
     "Sakura Chiyono O",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/10/577274.jpg",
    ),(
     "Yaeno Muteki",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/4/577273.jpg",
    ),(
     "Mejiro Ardan",
     "Uma Musume",
     "https://cdn.myanimelist.net/images/characters/6/577276.jpg",
    ),(
     "Nejire Hadou",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/2/549468.jpg",
    ),(
     "Camie Utsushimi",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/5/360253.jpg",
    ),(
     "Mitsuki Bakugou",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/3/359201.jpg",
    ),(
     "Itsuka Kendou",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/5/366577.jpg",
    ),(
     "Inko Midoriya",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/4/510381.jpg",
    ),(
     "Nana Shimura",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/4/361251.jpg",
    ),(
     "Mirko",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/11/602198.jpg",
    ),(
     "Eri",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/8/437981.jpg",
    ),(
     "Kaina Tsutsumi",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/16/501763.jpg",
    ),(
     "Star and Stripe",
     "My Hero Academia",
     "https://cdn.myanimelist.net/images/characters/11/507077.jpg",
    ),(
     "Neptune",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/16/299873.jpg",
    ),(
     "Noire",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/8/222923.jpg",
    ),(
     "Pupurut",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/3/222937.jpg",
    ),(
     "Nepgear",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/10/222929.jpg",
    ),(
     "Blanc",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/7/222925.jpg",
    ),(
     "Uni",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/14/222931.jpg",
    ),(
     "Vert",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/12/222927.jpg",
    ),(
     "IF",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/10/206095.jpg",
    ),(
     "Compa",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/7/594279.jpg",
    ),(
     "Ram (HN)",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/11/222933.jpg",
    ),(
     "Pish",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/7/222941.jpg",
    ),(
     "Histoire",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/5/206097.jpg",
    ),(
     "5pb.",
     "Hyperdimension Neptunia",
     "https://cdn.myanimelist.net/images/characters/13/215143.jpg",
    ),(
     "Mikoto Misaka",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/16/345046.jpg",
    ),(
     "Kuroko Shirai",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/13/69380.jpg",
    ),(
     "Last Order",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/5/112393.jpg",
    ),(
     "Index Librorum Prohibitorum",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/3/109007.jpg",
    ),(
     "MISAKA 10032",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/2/73911.jpg",
    ),(
     "Kaori Kanzaki",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/16/37716.jpg",
    ),(
     "Komoe Tsukuyomi",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/11/101005.jpg",
    ),(
     "Aisa Himegami",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/7/37948.jpg",
    ),(
     "Kazari Uiharu",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/3/65711.jpg",
    ),(
     "Mitsuko Kongou",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/7/396740.jpg",
    ),(
     "Itsuwa",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/10/109407.jpg",
    ),(
     "Seiri Fukiyose",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/2/109979.jpg",
    ),(
     "Shizuri Mugino",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/5/210225.jpg",
    ),(
     "Saiai Kinuhata",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/8/210223.jpg",
    ),(
     "Ruiko Saten",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/13/405744.jpg",
    ),(
     "Misaki Shokuhou",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/14/396278.jpg",
    ),(
     "Frenda Seivelun",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/11/208751.jpg",
    ),(
     "Shinobu Nunotaba",
     "Toaru",
     "https://cdn.myanimelist.net/images/characters/3/203015.jpg",
    ),(
     "Asuka Langley Souryuu",
     "Neon Genesis Evangelion",
     "https://cdn.myanimelist.net/images/characters/7/64541.jpg",
    ),(
     "Rei Ayanami",
     "Neon Genesis Evangelion",
     "https://cdn.myanimelist.net/images/characters/11/314932.jpg",
    ),(
     "Misato Katsuragi",
     "Neon Genesis Evangelion",
     "https://cdn.myanimelist.net/images/characters/14/80156.jpg",
    ),(
     "Ritsuko Akagi",
     "Neon Genesis Evangelion",
     "https://cdn.myanimelist.net/images/characters/13/108139.jpg",
    ),(
     "Yui Ikari",
     "Neon Genesis Evangelion",
     "https://cdn.myanimelist.net/images/characters/2/88927.jpg",
    ),(
     "Maya Ibuki",
     "Neon Genesis Evangelion",
     "https://cdn.myanimelist.net/images/characters/7/78694.jpg",
    ),(
     "Miho Azuki",
     "Bakuman",
     "https://cdn.myanimelist.net/images/characters/7/101585.jpg",
    ),(
     "Kaya Miyoshi",
     "Bakuman",
     "https://cdn.myanimelist.net/images/characters/15/106801.jpg",
    ),(
     "Yuriko Aoki",
     "Bakuman",
     "https://cdn.myanimelist.net/images/characters/6/193583.jpg",
    ),(
     "Misa Amane",
     "Death Note",
     "https://cdn.myanimelist.net/images/characters/15/96320.jpg",
    ),(
     "Naomi Misora",
     "Death Note",
     "https://cdn.myanimelist.net/images/characters/4/146595.jpg",
    ),(
     "Tatsumaki",
     "One Punch Man",
     "https://cdn.myanimelist.net/images/characters/5/379084.jpg",
    ),(
     "Fubuki",
     "One Punch Man",
     "https://cdn.myanimelist.net/images/characters/5/294843.jpg",
    ),(
     "Rize Kamishiro",
     "Tokyo Ghoul",
     "https://cdn.myanimelist.net/images/characters/15/251965.jpg",
    ),(
     "Hinami Fueguchi",
     "Tokyo Ghoul",
     "https://cdn.myanimelist.net/images/characters/8/258241.jpg",
    ),(
     "Touka Kirishima",
     "Tokyo Ghoul",
     "https://cdn.myanimelist.net/images/characters/15/269993.jpg",
    ),(
     "Saiko Yonebayashi",
     "Tokyo Ghoul",
     "https://cdn.myanimelist.net/images/characters/13/362131.jpg",
    ),(
     "Sen Takatsuki",
     "Tokyo Ghoul",
     "https://cdn.myanimelist.net/images/characters/2/285247.jpg",
    ),(
     "Nobara Kugisaki",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/2/521632.jpg",
    ),(
     "Maki Zenin",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/11/531387.jpg",
    ),(
     "Kasumi Miwa",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/5/431905.jpg",
    ),(
     "Mei Mei",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/8/435405.jpg",
    ),(
     "Shouko Ieiri",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/4/541948.jpg",
    ),(
     "Utahime Iori",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/3/435404.jpg",
    ),(
     "Yuki Tsukumo",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/5/531741.jpg",
    ),(
     "Mai Zenin",
     "Jujutsu Kaisen",
     "https://cdn.myanimelist.net/images/characters/11/444564.jpg",
    ),(
     "Nico Robin",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/16/363700.jpg",
    ),(
     "Nami",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/2/263249.jpg",
    ),(
     "Boa Hancock",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/14/146013.jpg",
    ),(
     "Yamato",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/9/486931.jpg",
    ),(
     "Carrot",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/11/353512.jpg",
    ),(
     "Perona",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/12/93698.jpg",
    ),(
     "Uta",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/11/506689.jpg",
    ),(
     "Vivi Nefertari",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/6/543874.jpg",
    ),(
     "Bonney Jewelry",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/14/146045.jpg",
    ),(
     "Reiju Vinsmoke",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/6/343184.jpg",
    ),(
     "Ulti",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/8/453421.jpg",
    ),(
     "Tashigi",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/2/266983.jpg",
    ),(
     "Monet",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/8/235837.jpg",
    ),(
     "Linlin Charlotte",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/14/337166.jpg",
    ),(
     "Shirahoshi",
     "One Piece",
     "https://cdn.myanimelist.net/images/characters/9/172487.jpg",
    ),(
     "Shouko Nishimiya",
     "A Silent Voice",
     "https://cdn.myanimelist.net/images/characters/2/344790.jpg",
    ),(
     "Naoka Ueno",
     "A Silent Voice",
     "https://cdn.myanimelist.net/images/characters/2/316403.jpg",
    ),(
     "Yuzuru Nishimiya",
     "A Silent Voice",
     "https://cdn.myanimelist.net/images/characters/10/330472.jpg",
    ),(
     "Miyako Ishida",
     "A Silent Voice",
     "https://cdn.myanimelist.net/images/characters/6/330353.jpg",
    ),(
     "C.C.",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/13/33815.jpg",
    ),(
     "Kallen Stadtfeld",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/8/31533.jpg",
    ),(
     "Shirley Fenette",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/7/33794.jpg",
    ),(
     "Euphemia Li Britannia",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/13/83313.jpg",
    ),(
     "Cornelia Li Britannia",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/9/474071.jpg",
    ),(
     "Nunnally Lamperouge",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/12/61334.jpg",
    ),(
     "Villetta Nu",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/15/83310.jpg",
    ),(
     "Anya Alstreim",
     "Code Geass",
     "https://cdn.myanimelist.net/images/characters/6/83435.jpg",
    ),(
     "Hiyori Iki",
     "Noragami",
     "https://cdn.myanimelist.net/images/characters/16/573518.jpg",
    ),(
     "Bishamon",
     "Noragami",
     "https://cdn.myanimelist.net/images/characters/13/237153.jpg",
    ),(
     "Kofuku",
     "Noragami",
     "https://cdn.myanimelist.net/images/characters/15/234245.jpg",
    ),(
     "Nora",
     "Noragami",
     "https://cdn.myanimelist.net/images/characters/6/234239.jpg",
    ),(
     "Kayo Hinazuki",
     "Erased",
     "https://cdn.myanimelist.net/images/characters/9/300610.jpg",
    ),(
     "Sachiko Fujinuma",
     "Erased",
     "https://cdn.myanimelist.net/images/characters/5/300491.jpg",
    ),(
     "Airi Katagiri",
     "Erased",
     "https://cdn.myanimelist.net/images/characters/14/299245.jpg",
    )
]



testGirls = [
    (  #543
     "Michiru Kinushima",
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/5/280701.jpg",
    ),(  #544
     "Eru Miru",
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/8/280702.jpg",
    ),(  #545
     "Kazuki Kuwanomi",
     "Plastic Memories",
     "https://cdn.myanimelist.net/images/characters/12/280704.jpg",
    ),(  #546
     "Akane Kurokawa",
     "Oshi no Ko",
     "https://media.discordapp.net/attachments/1422438714730217482/1423061165101158472/Akane_Kurokawa.jpg"
    ),(  #547
     "Fern",
     "Frieren: Beyond Journey's End",
     "https://media.discordapp.net/attachments/1422438714730217482/1423054988330008708/Fern.jpg?"
    ),(  #914
     "Leafa",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/5/254605.jpg",
    ),(  #915
     "Yui",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/15/264165.jpg",
    ),(  #916
     "Keiko Ayano",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/10/185423.jpg",
    ),(  #917
     "Rika Shinozaki",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/8/177115.jpg",
    ),(  #918
     "Sachi",
     "Sword Art Online",
     "https://cdn.myanimelist.net/images/characters/7/264145.jpg",
    )#,(
     #"",
     #"",
     #"",
    #)
]



girlDictionary = {name.lower(): {"name": name, "show": show, "url": url} for name, show, url in girls}
showDictionary = defaultdict(list)

for name, show, url in girls:
    showDictionary[show.lower()].append({"name": name, "show": show, "url": url})




def randomGirlGen(n = 1):
    return random.sample(girls, n)

def testGirlGen(n = 1):
    return random.sample(testGirls, n)