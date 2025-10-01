import os
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
    ("Akane Kurokawa", "https://media.discordapp.net/attachments/1422438714730217482/1423061165101158472/Akane_Kurokawa.jpg?ex=68def07c&is=68dd9efc&hm=4f4be2584947258c0a8ffddee51172d79df8442171cddacf992621c32e2b0409&=&format=webp&width=450&height=700"),
    ("Maomao", "https://media.discordapp.net/attachments/1422438714730217482/1423060210318180542/Maomao.jpg?ex=68deef99&is=68dd9e19&hm=bb210d6dba9456d9ca892692a686dd0f1f04f389ad54d1c3fe845b2dea572406&=&format=webp&width=900&height=1400")
]



def randomGirlGen():
    #images = get_girl_image_list()
    return random.choice(girls)