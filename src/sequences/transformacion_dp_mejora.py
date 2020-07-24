from dp import  *
from blocks import *
from luma import *
from bclass import *

def dp_matrix(img1,img2, line):
    A = luma(img1)
    B = luma(img2)

    accumA = 0
    accumB = 0
    wTotal = 0
    matchings =[]
    block_sizes_A = []
    block_sizes_B = []

    mb = MatchingBlocks()
    
    blocks_base_A = getBase(A[line])
    A[line] = getBlocks(A[line],len(A[line]))
    block_sizes_A.append(A[line])
    
    blocks_base_B = getBase(B[line])
    B[line] = getBlocks(B[line],len(B[line]))
    block_sizes_B.append(B[line])

    mb.a_blocks_sizes = A[line]
    mb.b_blocks_sizes = B[line]
    mb.a_blocks_coordinates = blocks_base_A
    mb.b_blocks_coordinates = blocks_base_B

    accumA = len(A)
    accumB = len(B)                

    mu = accumA/accumB

    temp1, temp2 = minMatchingDP(A[line],B[line],mu)

    matchings.append(temp1)
    wTotal += temp2

    return matchings, wTotal, mb