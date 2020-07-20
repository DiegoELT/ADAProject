from luma import luma
from transformacion_voraz import greedy_matrix
from transformacion_dp import dp_matrix

import sys # This is used for providing the code with an extra argument if needed.
import time # For actual experimentation and timing, has not been used to measure actual O-notation though. 
import math

def readingImages(img_name_1, img_name_2): 
  coded_img_1 = luma(img_name_1)
  coded_img_2 = luma(img_name_2)
  return coded_img_1, coded_img_2

if(len(sys.argv) == 1): # In other words, if no file is provided
  print("Default images are being used.")
  img1 = 'arnold.png'
  img2 = 'bush.png'
elif(len(sys.argv) != 3):
  print("Please provide 2 file names for the images.")
else:
  img1 = sys.argv[1]
  img2 = sys.argv[2]

a_sequences, b_sequences = readingImages(img1, img2)

# Here is where the actual animation process takes place

# Testing matrix sizes

print("A matrix size: ", len(a_sequences))
print("B matrix size: ", len(b_sequences))

match, w = greedy_matrix(img1, img2)

print(match, w)