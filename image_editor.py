#!/usr/bin/env python3

# imports required modules
import os, sys
from PIL import Image

"""
Script to iterate over directory of images in order to modify them to specifications for upload:
128x128 image resolution, 90 degrees clockwise, .jpeg format
Then save them into a different directory
"""

# initializes source and destination paths
src_path = os.path.expanduser('~') + "/images/"
dst_path = "/opt/icons/"

os.chdir(src_path)
# iterates over files in that directory
for root, dirs, files in os.walk("."):
    for file in files:
        # splits the path name into a pair file name and ext
        f, e = os.path.splitext(file)
        # initializes source and destination file paths using path and file name
        infile = os.path.join(src_path,f)
        outfile = os.path.join(dst_path,f)
        try:
            # opens image
            with Image.open(infile) as im:
                # modifies image to specified image resolution, orientation, and format
                new_im = im.resize((128,128))
                new_im = new_im.rotate(-90)
                new_im = new_im.convert('RGB')
                # saves image as JPEG in correct directory
                new_im = new_im.save(outfile + ".jpeg")
        # raises and prints an exception if error occurs
        except (IOError, OSError):
            print("Cannot convert", infile)
