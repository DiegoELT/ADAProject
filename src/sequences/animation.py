from luma import luma, imageio
from transformacion_voraz import greedy_matrix
from transformacion_dp import dp_matrix
from bclass import *
from matplotlib import pyplot as PLT


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

super_image = []

final_weight = 0

for x in range (len(a_sequences)):
  
  match, w, mb = greedy_matrix(img1, img2, x)
  final_weight += w 

  print(mb.a_blocks_coordinates, " - ", mb.b_blocks_coordinates)

  polygon_attempt = mb.proportional_matching(match[0],1)

  iterations = 1

  intermediate_matrix_line = []

  for i in range(iterations):
    intermediate = []
    for j in range(len(a_sequences[0])):
      pixel = Polygon([(i,j),(i+1,j),(i+1,j+1),(i,j+1)])
      intermediate.append(pixel)
    intermediate_matrix_line.append(intermediate)

  print(len(polygon_attempt))

  image_a = imageio.imread(img1)[x]
  image_intermediate = []
  image_b = imageio.imread(img2)[x]

  for i in range(len(a_sequences[0])):
    pixel_rgb = [0,0,0]
    image_intermediate.append(pixel_rgb)
    for j in range(3):
      image_intermediate[i][j]=image_a[i][j]

  #print("Before!")
  #print(image_intermediate)

  counter = 0
  for i in range(iterations):
    for j in range(len(a_sequences[0])):
      for k in polygon_attempt:
        if (intermediate_matrix_line[i][j].intersects(k)):
          counter += 1
          pixel = math.floor(k.exterior.coords[2][0])
          if pixel >= (len(a_sequences)):
            pixel = len(a_sequences)-1
          image_intermediate[j][0] = round((image_intermediate[j][0] + image_b[pixel][0])/2)
          image_intermediate[j][1] = round((image_intermediate[j][1] + image_b[pixel][0])/2)
          image_intermediate[j][2] = round((image_intermediate[j][2] + image_b[pixel][0])/2)
            
  #print("After! ", counter, " modifications.")
  #print(image_intermediate)

  super_image.append(image_intermediate)

PLT.imshow(super_image)
PLT.show()

print("Weight of the whole thing is: ", final_weight)