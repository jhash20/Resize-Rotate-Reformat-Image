#!/usr/bin/env python3

"""Script that processes directory of images and modifies to specifications for upload:
128x128 image resolution, 90 degrees clockwise, .jpeg format
Then saves them into a different directory
"""

import os, sys
from PIL import Image


src_path = os.path.expanduser('~') + "/images/"
dst_path = "/opt/icons/"
os.chdir(src_path)

# iterates over files in directory
for root, dirs, files in os.walk("."):
    for file in files:
        f, e = os.path.splitext(file)
        infile = os.path.join(src_path,f)
        outfile = os.path.join(dst_path,f)
        try:
            # opens/modifies image to specifications
            with Image.open(infile) as im:
                new_im = im.resize((128,128))
                new_im = new_im.rotate(-90)
                new_im = new_im.convert("RGB")
                # saves image as JPEG in correct directory
                new_im = new_im.save(outfile + ".jpeg")
        except (IOError, OSError):
            print("Cannot convert", infile)
