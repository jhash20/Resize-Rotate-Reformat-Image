#!/usr/bin/env python3

# import required modules
import os, sys
from PIL import Image

new_path = "/opt/icons/"

os.chdir(directory)
# iterate over files in that directory
for root, dirs, files in os.walk(".")
    for file in files:
        # splits the path name into a pair root and ext
        f, e = os.path.splitext(file)
        try:
            # open image
            im = Image.open(file)
            # modify image
            new_im = im.resize((128,128))
            new_im = im.rotate(-90)
            new_im = im.convert('RGB')
            # save image as JPEG in correct directory
            new_im = im.save(new_path) + str(f) + ".jpg")
        except OSError:
            print("cannot convert", infile)
