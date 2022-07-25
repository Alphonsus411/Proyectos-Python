from pickletools import optimize
from PIL import Image


import os

DOWNLOAD_FOLDER = "downloads"

if __name__ == '__main__':
    for filename in os.listdir(DOWNLOAD_FOLDER):
        name, extension = os.path.splitext(DOWNLOAD_FOLDER + "/" + filename)
        
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(DOWNLOAD_FOLDER + "/" + filename)
            picture.save(DOWNLOAD_FOLDER + "compresed/" + filename, optimize = True, quality = 60)
            