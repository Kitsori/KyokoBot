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
    ("Fern", "https://media.discordapp.net/attachments/1422438714730217482/1423054988330008708/Fern.jpg?")
]



def randomGirlGen():
    #images = get_girl_image_list()
    return random.choice(girls)