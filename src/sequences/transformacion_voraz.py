from greedy import  *
from blocks import *
from luma import *

def greedy_matrix(img1,img2):
    A = luma(img1)
    B = luma(img2)
    	
    total_weight = 0
    matchings = []
    block_sizes_A = []
    block_sizes_B = []

    for i in range(1):
    
        blocksA = getBlocks(A[i], len(A[i]))
        block_sizes_A.append(blocksA)
        blocks_base_A = getBase(A[i])
        blocksB = getBlocks(B[i], len(B[i]))
        block_sizes_B.append(blocksB)
        blocks_base_B = getBase(B[i])

        print("Bloques A: ", blocksA)
        print("Coordenadas A: ",blocks_base_A)
        print("Bloques B: ", blocksB)
        print("Coordenadas B: ",blocks_base_B)

        line_matchings, line_weight = minMatchingGreedy(blocksA,blocksB)

        matchings.append(line_matchings)
        total_weight += line_weight

    return matchings, total_weight