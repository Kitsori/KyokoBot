import os
import random

IMAGE_FOLDER = "Girls"

def get_girl_image_list():

    images = []

    for filename in os.listdir(IMAGE_FOLDER):
        if filename.lower().endswith((".jpg")):
            name = os.path.splitext(filename)[0]
            path = os.path.join(IMAGE_FOLDER, filename)
            images.append((name, path))
    return images



def randomGirlGen():
    images = get_girl_image_list()
    return random.choice(images)