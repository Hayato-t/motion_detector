# Picture converter
# by Hayato Tsunoda
# 
# Converting all pictures in selected file to simulation input text file

# example:
# python picture_encoder.py [INPUT_DIR_PATH] [WIDTH] [HEIGHT] [OUTPUT_FILE_NAME]
# pick up all .bmp files in FILEPATH, convert them into gray scale WIDTH * HEIGHT, and save it to text file
# outout file is tab-delimited and each row correspond to input picture.
# N th row is a N th .bmp file in ordered by name
# The number of columns is WIDTH * HEIGHT

import sys
import glob
import re
from PIL import Image
from PIL import ImageOps
import numpy as np
import codecs

args = sys.argv

if len(args) != 5:
    print("ERROR: 4 argments are required for this program")
    sys.exit()
input_filepath = args[1]
width = int(args[2])
height = int(args[3])
output_filename = args[4]
if re.match("/$",input_filepath) is None:
    files = glob.glob(input_filepath + "/" + "*.bmp")
else:
    files = glob.glob(input_filepath + "*.bmp")

if len(files) == 0:
    print("ERROR: no bmp file in " + input_filepath + ".")
    sys.exit()

files.sort()

fout = codecs.open(output_filename,'w','utf-8')

for i,file in enumerate(files):
    print("Progress:" + str(i+1) + "/" + str(len(files)))
    img = Image.open(file)
    gray_img = img.convert("L")
    resized_img = gray_img.resize((int(width),int(height)))
    for h in range(0,height):
        for w in range(0,width):
            fout.write(str(resized_img.getpixel((w,h))/255.0))
            if h != height-1 or w != width-1:
                print("wrotetab: w={0},h={1}\n".format(w,h))
                fout.write('\t')
    fout.write('\n')

fout.close()
print("Convertion Complete.")
