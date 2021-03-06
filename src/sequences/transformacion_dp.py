from dp import  *
from blocks import *
from luma import *
from bclass import *

def dp_matrix(img1,img2, line):
    A = luma(img1)
    B = luma(img2)
    	
    wTotal = 0
    matchings =[]
    block_sizes_A = []
    block_sizes_B = []

    mb = MatchingBlocks()
        
    blocksA = getBlocks(A[line],len(A[line]))
    block_sizes_A.append(blocksA)
    blocks_base_A = getBase(A[line])

    blocksB = getBlocks(B[line],len(B[line]))
    block_sizes_B.append(blocksB)
    blocks_base_B = getBase(B[line])

    mb.a_blocks_sizes = blocksA
    mb.b_blocks_sizes = blocksB
    mb.a_blocks_coordinates = blocks_base_A
    mb.b_blocks_coordinates = blocks_base_B

    if(len(blocksB) == 0):
      print("The Luma coefficient is too high, please input a smaller value.")
    
    temp1, temp2 = minMatchingDP(blocksA,blocksB,0)

    matchings.append(temp1)
    wTotal += temp2

    return matchings, wTotal, mb