import random

IMAGE_FOLDER = "Girls"

#def get_girl_image_list():

#    images = []

#    for filename in os.listdir(IMAGE_FOLDER):
#        if filename.lower().endswith((".jpg")):
#            name = os.path.splitext(filename)[0]
#            path = os.path.join(IMAGE_FOLDER, filename)
#            images.append((name, path))
#    return images

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



def randomGirlGen():
    #images = get_girl_image_list()
    return random.choice(girls)