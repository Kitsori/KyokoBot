import random


# The Huge List of Anime Girls - Grouped by shows listed on the right
girls = [
    ("Miku Nakano", "https://media.discordapp.net/attachments/1423388983915708558/1423447921679925258/457434.png?"),     # Quintessential Quintuplets
    ("Nino Nakano", "https://media.discordapp.net/attachments/1422999881269645424/1423057873512042626/Nino_Nakano.jpg?"),
    ("Itsuki Nakano", "https://media.discordapp.net/attachments/1423388983915708558/1423448069361369198/433646.png?"),
    ("Yotsuba Nakano", "https://media.discordapp.net/attachments/1423388983915708558/1423448402925981897/433645.png?"),
    ("Ichika Nakano", "https://media.discordapp.net/attachments/1423388983915708558/1423448540226523186/433644.png?"),
    ("Raiha Uesugi", "https://media.discordapp.net/attachments/1423388983915708558/1423448636733526227/555613.png?"),
    ("Vladilena Milize", "https://media.discordapp.net/attachments/1423388983915708558/1423454888649556099/428175.png?"), # 86 Eighty Six
    ("Anju Emma", "https://media.discordapp.net/attachments/1423388983915708558/1423455070686679130/435464.png?"),
    ("Kurena Kukumila", "https://media.discordapp.net/attachments/1423388983915708558/1423455154266705950/435472.png?"),
    ("Frederica Rosenfort", "https://media.discordapp.net/attachments/1423388983915708558/1423455306314158130/453080.png?"),
    ("Kanade Tachibana", "https://media.discordapp.net/attachments/1423388983915708558/1423457496072327173/241395.png?"), # Angel Beats
    ("Yuri Nakamura", "https://media.discordapp.net/attachments/1423388983915708558/1423457706395697253/91856.png?"),
    ("Yui", "https://media.discordapp.net/attachments/1423388983915708558/1423457779208687616/150391.png?"),
    ("Masami Iwasawa", "https://media.discordapp.net/attachments/1423388983915708558/1423457848767156334/117224.png?"),
    ("Shiina", "https://media.discordapp.net/attachments/1423388983915708558/1423457897727262863/110858.png?"),
    ("Meiko Honma", "https://media.discordapp.net/attachments/1423388983915708558/1423462507330273290/115711.png?"),     # Anohana
    ("Naruko Anjou", "https://media.discordapp.net/attachments/1423388983915708558/1423462558031024259/121622.png?"),
    ("Chiriko Tsurumi", "https://media.discordapp.net/attachments/1423388983915708558/1423462603048353913/118054.png?"),
    ("Mei Misaki", "https://media.discordapp.net/attachments/1423388983915708558/1423463685086515211/237389.png?"),      #Another
    ("Izumi Akazawa", "https://media.discordapp.net/attachments/1423388983915708558/1423463734763851796/155667.png?"),
    ("Kaede Kayano", "https://media.discordapp.net/attachments/1423388983915708558/1423464238667661377/274395.png?"),    # Assassination Classroom
    ("Irina Jelavic", "https://media.discordapp.net/attachments/1423388983915708558/1423464285304000523/276605.png?"),
    ("Rio Nakamura", "https://media.discordapp.net/attachments/1423388983915708558/1423464375758622770/277161.png?"),
    ("Ritsu Hayasaka", "https://media.discordapp.net/attachments/1423388983915708558/1423464319458480218/277977.png?"),
    ("Hinano Kurahashi", "https://media.discordapp.net/attachments/1423388983915708558/1423464411917451324/276606.png?"),
    ("Yue", "https://media.discordapp.net/attachments/1423388983915708558/1423465491258933358/407199.png?"),             # Arifureta
    ("Kaori Shirasaki", "https://media.discordapp.net/attachments/1423388983915708558/1423465944142839879/558844.png?"),
    ("Tio Klarus", "https://media.discordapp.net/attachments/1423388983915708558/1423465979198967868/371438.png?"),
    ("Shea Haulia", "https://media.discordapp.net/attachments/1423388983915708558/1423466020848533668/371437.png?"),
    ("Myuu", "https://media.discordapp.net/attachments/1423388983915708558/1423466055954600079/568863.png?"),
    ("Shizuku Yaegashi", "https://media.discordapp.net/attachments/1423388983915708558/1423466086895980667/402101.png?"),
    ("Suzu Taniguchi", "https://media.discordapp.net/attachments/1423388983915708558/1423466199261642752/568866.png?"),
    ("Liliana Heiligh", "https://media.discordapp.net/attachments/1423388983915708558/1423466279372853539/480478.png?"),
    ("Minami Shimada", "https://media.discordapp.net/attachments/1423388983915708558/1423467612108750858/77138.png?"),   # Baka And Test
    ("Shouko Kirishima", "https://media.discordapp.net/attachments/1423388983915708558/1423467670506045581/96539.png?"),
    ("Mizuki Himeji", "https://media.discordapp.net/attachments/1423388983915708558/1423467712717520936/110667.png?"),
    ("Yuuko Kinoshita", "https://media.discordapp.net/attachments/1423388983915708558/1423467753427435521/76945.png?"),
    ("Akira Yoshii", "https://media.discordapp.net/attachments/1423388983915708558/1423467793222996009/85307.png?"),
    ("Rinrada Ratchamanee", "https://media.discordapp.net/attachments/1423388983915708558/1423468350050275398/598468.png?"), # Baan
    ("Michiru Kagemori", "https://media.discordapp.net/attachments/1423388983915708558/1423468715365896323/408681.png?"), # BNA
    ("Nazuna Hiwatashi", "https://media.discordapp.net/attachments/1423388983915708558/1423468943095365694/367f5af87785e65cf6db80132cca0c0c.png?"),
    ("Hitori Gotou", "https://media.discordapp.net/attachments/1423388983915708558/1423469539089453137/491455.png?"),    # Bocchi The Rock!
    ("Ryou Yamada", "https://media.discordapp.net/attachments/1423388983915708558/1423469610660790454/544161.png?"),
    ("Nijika Ijichi", "https://media.discordapp.net/attachments/1423388983915708558/1423469651987529779/544158.png?"),
    ("Kita Ikuyo", "https://media.discordapp.net/attachments/1423388983915708558/1423469714004250715/495135.png?"),
    ("Kikuri Hiroi", "https://media.discordapp.net/attachments/1423388983915708558/1423469756278640670/493846.png?"),
    ("PA-san", "https://media.discordapp.net/attachments/1423388983915708558/1423469791397544049/502200.png?"),
    ("Seika Ijichi", "https://media.discordapp.net/attachments/1423388983915708558/1423469833969864774/490794.png?"),
    ("Futari Gotou", "https://media.discordapp.net/attachments/1423388983915708558/1423469872536490024/493791.png?"),
    ("Ochako Uraraka", "https://media.discordapp.net/attachments/1423388983915708558/1423471164650688674/309105.png?"),  # My Hero Academia
    ("Himiko Toga", "https://media.discordapp.net/attachments/1423388983915708558/1423471228454436915/485281.png?"),
    ("Tsuyu Asui", "https://media.discordapp.net/attachments/1423388983915708558/1423471341851643997/343086.png?"),
    ("Kyouka Jirou", "https://media.discordapp.net/attachments/1423388983915708558/1423471458050506762/309100.png?"),
    ("Momo Yaoyorozu", "https://media.discordapp.net/attachments/1423388983915708558/1423471547712012398/562316.png?"),
    ("Mina Ashido", "https://media.discordapp.net/attachments/1423388983915708558/1423471623817793651/329525.png?"),
    ("Nemuri Kayama", "https://media.discordapp.net/attachments/1423388983915708558/1423471711717953708/366576.png?"),
    ("Tooru Hagakure", "https://media.discordapp.net/attachments/1423388983915708558/1423471797382418452/301045.png?"),
    ("Yuu Takeyama", "https://media.discordapp.net/attachments/1423388983915708558/1423471852713545838/301651.png?"),
    ("Mei Hatsume", "https://media.discordapp.net/attachments/1423388983915708558/1423472444617789512/517350.png?"),
    ("Anna Yamada", "https://media.discordapp.net/attachments/1423388983915708558/1423472864362758254/536836.png?"),     # BokuYaba
    ("Kana Ichikawa", "https://media.discordapp.net/attachments/1423388983915708558/1423472899393720430/578723.png?"),
    ("Moeko Sekine", "https://media.discordapp.net/attachments/1423388983915708558/1423472927940022424/569420.png?"),
    ("Chihiro Kobayashi", "https://media.discordapp.net/attachments/1423388983915708558/1423472954267664474/533899.png?"),
    ("Honoka Hara", "https://media.discordapp.net/attachments/1423388983915708558/1423472982096875582/533894.png?"),
    ("Sena Kashiwazaki", "https://media.discordapp.net/attachments/1423388983915708558/1423473581630820352/132291.png?"), # Haganai
    ("Yozora Mikazuki", "https://media.discordapp.net/attachments/1423388983915708558/1423473639981842532/150969.png?"),
    ("Rika Shiguma", "https://media.discordapp.net/attachments/1423388983915708558/1423473754541002802/198519.png?"),
    ("Kobato Hasegawa", "https://media.discordapp.net/attachments/1423388983915708558/1423473696789495850/146645.png?"),
    ("Maria Takayama", "https://media.discordapp.net/attachments/1423388983915708558/1423473786757451786/178131.png?"),
    ("Kate Takayama", "https://media.discordapp.net/attachments/1423388983915708558/1423473896249884713/193475.png?"),
    ("Yukimura Kusunoki", "https://media.discordapp.net/attachments/1423388983915708558/1423473835419635722/205391.png?"),
    ("Uta", "https://media.discordapp.net/attachments/1423388983915708558/1423474993659908147/466809.png?"),              # Bubble
    ("Power", "https://media.discordapp.net/attachments/1423388983915708558/1423475566706954341/494969.png?"),            # Chainsaw Man
    ("Makima", "https://media.discordapp.net/attachments/1423388983915708558/1423475614886662154/494972.png?"),
    ("Reze", "https://media.discordapp.net/attachments/1423388983915708558/1423475660868812820/574771.png?"),
    ("Kobeni Higashiyama", "https://media.discordapp.net/attachments/1423388983915708558/1423475693504827422/533497.png?"),
    ("Himeno", "https://media.discordapp.net/attachments/1423388983915708558/1423475724190224455/492411.png?"),
    ("Nao Tomori", "https://media.discordapp.net/attachments/1423388983915708558/1423476465886036079/288019.png?"),       # Charlotte
    ("Ayumi Otosaka", "https://media.discordapp.net/attachments/1423388983915708558/1423476554528194580/288021.png?"),
    ("Yusa Kurobane", "https://media.discordapp.net/attachments/1423388983915708558/1423476637483139092/288018.png?"),
    ("Misa Kurobane", "https://media.discordapp.net/attachments/1423388983915708558/1423476679682293862/341989.png?"),
    ("Nagisa Furukawa", "https://media.discordapp.net/attachments/1423388983915708558/1423484016136556614/300961.png?"),  # Clannad
    ("Ushio Okazaki", "https://media.discordapp.net/attachments/1423388983915708558/1423484059186892899/382211.png?"),
    ("Tomoyo Sakagami", "https://media.discordapp.net/attachments/1423388983915708558/1423484104355221525/34293.png?"),
    ("Kyou Fujibayashi", "https://media.discordapp.net/attachments/1423388983915708558/1423484184034283551/70221.png?"),
    ("Fuuko Ibuki", "https://media.discordapp.net/attachments/1423388983915708558/1423484237021057064/79593.png?"),
    ("Kotomi Ichinose", "https://media.discordapp.net/attachments/1423388983915708558/1423484310564110427/79587.png?"),
    ("Sanae Furukawa", "https://media.discordapp.net/attachments/1423388983915708558/1423484356365652130/54058.png?"),
    ("Ryou Fujibayashi", "https://media.discordapp.net/attachments/1423388983915708558/1423484391413518386/256501.png?"),
    ("Mei Sunohara", "https://media.discordapp.net/attachments/1423388983915708558/1423484431695347765/35087.png?"),
    ("Misae Sagara", "https://media.discordapp.net/attachments/1423388983915708558/1423484470576680991/382201.png?"),
    ("Lucy", "https://media.discordapp.net/attachments/1423388983915708558/1423485741962362911/486620.png?"),             # Cyberpunk Edgerunners
    ("Rebecca", "https://media.discordapp.net/attachments/1423388983915708558/1423485801727135924/547499.png?"),
    ("Akane Kurokawa", "https://media.discordapp.net/attachments/1422438714730217482/1423061165101158472/Akane_Kurokawa.jpg"),  # MISC.
    ("Maomao", "https://media.discordapp.net/attachments/1422438714730217482/1423060210318180542/Maomao.jpg?"),
    ("Yoshino", "https://media.discordapp.net/attachments/1422438714730217482/1423060152835248341/Yoshino.jpg?"),
    ("Ai Fuyuumi", "https://media.discordapp.net/attachments/1422438714730217482/1423060101169938605/Ai_Fuyuumi.jpg?"),
    ("Fern", "https://media.discordapp.net/attachments/1422438714730217482/1423054988330008708/Fern.jpg?"),
    ("Mukuro Hoshimiya", "https://media.discordapp.net/attachments/1422999881269645424/1423058083743137905/Mukuro_Hoshimiya.jpg?"),
    ("Yuuko Yoshida", "https://media.discordapp.net/attachments/1422999881269645424/1423057957246996581/Yuuko_Yoshida.jpg?"),
    ("Nino Nakano", "https://media.discordapp.net/attachments/1422999881269645424/1423057873512042626/Nino_Nakano.jpg?"),
    ("Karane Inda", "https://media.discordapp.net/attachments/1422999881269645424/1423055211374579742/Karane_Inda.jpg?"),
    ("Hifumi Takimoto", "https://media.discordapp.net/attachments/1422999881269645424/1423013456369422376/Hifumi_Takimoto.jpg?")
]


def randomGirlGen(n = 1):
    #images = get_girl_image_list()
    return random.sample(girls, n)