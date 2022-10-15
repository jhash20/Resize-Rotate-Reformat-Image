#!/usr/bin/env python3

# import required modules
import os, sys
from PIL import Image

src_path = os.path.expanduser('~') + "/images/"
dst_path = "/opt/icons/"

os.chdir(src_path)
# iterate over files in that directory
for root, dirs, files in os.walk("."):
    for file in files:
        # splits the path name into a pair root and ext
        f, e = os.path.splitext(file)
        infile = os.path.join(src_path,f)
        outfile = os.path.join(dst_path,f)
        try:
            # open image
            with Image.open(infile) as im:
                # modify image
                new_im = im.resize((128,128))
                new_im = new_im.rotate(-90)
                new_im = new_im.convert('RGB')
                # save image as JPEG in correct directory
                new_im = new_im.save(outfile + ".jpg")
        except OSError:
            print("cannot convert", infile)
