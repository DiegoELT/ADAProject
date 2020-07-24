from greedy import  *
from blocks import *
from luma import *
from bclass import *

def greedy_matrix(img1,img2, line):
    A = luma(img1)
    B = luma(img2)
    	
    total_weight = 0
    matchings = []
    block_sizes_A = []
    block_sizes_B = []

    mb = MatchingBlocks()

    
    blocksA = getBlocks(A[line], len(A[line]))
    block_sizes_A.append(blocksA)
    blocks_base_A = getBase(A[line])
    blocksB = getBlocks(B[line], len(B[line]))
    block_sizes_B.append(blocksB)
    blocks_base_B = getBase(B[line])

    print("Bloques A: ", blocksA)
    print("Coordenadas A: ",blocks_base_A)
    print("Bloques B: ", blocksB)
    print("Coordenadas B: ",blocks_base_B)

    mb.a_blocks_sizes = blocksA
    mb.b_blocks_sizes = blocksB
    mb.a_blocks_coordinates = blocks_base_A
    mb.b_blocks_coordinates = blocks_base_B

    line_matchings, line_weight = minMatchingGreedy(blocksA,blocksB)

    matchings.append(line_matchings)
    total_weight += line_weight

    return matchings, total_weight, mb