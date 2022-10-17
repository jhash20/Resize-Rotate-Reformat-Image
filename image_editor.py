#!/usr/bin/env python3

# imports required modules
import os, sys
from PIL import Image

# initializes variables
src_path = os.path.expanduser('~') + "/images/"
dst_path = "/opt/icons/"

os.chdir(src_path)
# iterates over files in that directory
for root, dirs, files in os.walk("."):
    for file in files:
        # splits the path name into a pair root and ext
        f, e = os.path.splitext(file)
        infile = os.path.join(src_path,f)
        outfile = os.path.join(dst_path,f)
        try:
            # opens image
            with Image.open(infile) as im:
                # modifies image
                new_im = im.resize((128,128))
                new_im = new_im.rotate(-90)
                new_im = new_im.convert('RGB')
                # saves image as JPEG in correct directory
                new_im = new_im.save(outfile + ".jpg")
        except OSError:
            print("cannot convert", infile)
