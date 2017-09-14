# converted image viewer
#
#
# converted image viewer render converted image file and generate movie file

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as amt
import sys
import os.path
from PIL import Image

args = sys.argv

input_filename = args[1]
width = int(args[2])
height = int(args[3])

if not os.path.exists(input_filename):
    print("Error: " + input_filename + " is not exist.")
    exit()

f = open(input_filename, 'r')
datalines = f.read().split('n')
f.close()
picture_array = np.zeros((len(datalines),height,width))
for index,line in enumerate(datalines):
    datalist = line.split('\t')
    print(datalist)
    for i in range(height):
        for j in range(width):
            picture_array[index][i][j] = int(float(datalist[i * width + j]) * 255)
test = np.array(picture_array[0], dtype = np.uint8)
plt.imshow(test, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()
