from dp import  *
from blocks import *
from luma import *

def dp_matrix(img1,img2):
    A = luma(img1)
    B = luma(img2)

    accumA = 0
    accumB = 0
    wTotal = 0
    matchings =[]
    
    for i in range(len(A)):
        
        A[i] = getBlocks(A[i],len(A[i]))
        B[i] = getBlocks(B[i],len(B[i]))
        accumA = len(A)
        accumB = len(B)                

    mu = accumA/accumB

    for i in range(len(A)):

        temp1, temp2 = minMatchingDP(A[i],B[i],mu)
	
        matchings.append(temp1)
        wTotal += temp2

    return matchings, wTotal

match, w = dp_matrix('1.png','4.png')

print(match)
print(w)
