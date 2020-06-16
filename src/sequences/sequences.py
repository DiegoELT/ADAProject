# This is the main program for the impleementation of the algorithms. 
# Project by: Alejandro Goicochea, Diego Linares, and Ariana Villegas

import sys # This is used for providing the code with an extra argument if needed.
import time # For actual experimentation and timing, has not been used to measure actual O-notation though. 
import math

from blocks import getBlocks
from greedy import minMatchingGreedy
from memoization import minMatchingM
from recursive import minMatchingR

sampleA = [0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1]
sampleB = [0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0]

def algorithms(argument):
  switcher = {"g": minMatchingGreedy, "m": minMatchingM, "r": minMatchingR}
  func = switcher.get(argument, lambda: "Unknown Behaviour")
  return func(X,Y)

if(len(sys.argv) == 1): # In other words, if no file is provided
  while True: 
    response = input("Use sample values? (y/n)\n")
    if(response == "y" or response == "n"):
      break
  if(response == "n"):
    A = list(map(int, list(input("Insert the values for sequence A as a continuous string.\n"))))
    B = list(map(int, list(input("Insert the values for sequence B as a continuous string.\n"))))
  else:
    A = sampleA
    B = sampleB
else:
  file = open(sys.argv[1],'r')
  lines = file.read().splitlines() # There might be a way to do it without needing this line. But it works. 
  A = list(map(int,list(lines[0])))
  B = list(map(int,list(lines[1])))

# Then we get the length of each of the blocks we are going to use.
X = getBlocks(A,len(A))
Y = getBlocks(B,len(B))

while True:
  response = input("Select algorithm (g/m/r)\n")
  if(response == "g" or response == "m" or response == "r"):
    break

# Based on the response we got to the previous question we get a result.
start = time.time()
M, w = algorithms(response)
end = time.time()

print("The weight of the matching is: ", w)
print("The matching was: ", sorted(M))
print("\nExecution time was: ",end-start," seconds.")
