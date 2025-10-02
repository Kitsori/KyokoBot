import random

girls = [
    ("Akane Kurokawa", "https://media.discordapp.net/attachments/1422438714730217482/1423061165101158472/Akane_Kurokawa.jpg"),
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