from dp import  *
from blocks import *
from luma import *

def dp_matrix(img1,img2):
    A = luma(img1)
    B = luma(img2)
    	
    wTotal = 0
    matchings =[]

    for i in range(len(A)):
        
        blocksA = getBlocks(A[i],len(A[i]))
        blocksB = getBlocks(B[i],len(B[i]))

        temp1, temp2 = minMatchingDP(blocksA,blocksB)
	
        matchings.append(temp1)
        wTotal += temp2

    return matchings, wTotal

match, w = dp_matrix('1.png','4.png')

print(match)
print(w)
