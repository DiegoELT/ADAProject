from greedy import  *
from blocks import *

def greedy_matrix(A,B):
    wTotal = 0
    matchings =[]

    for i in range(len(A)):

        blocksA = getBlocks(A[i],len(A[i]))
        blocksB = getBlocks(B[i],len(B[i]))

        temp1, temp2 = minMatchingGreedy(blocksA,blocksB)

        matchings.append(temp1)
        wTotal += temp2

    return matchings, wTotal

A = [[0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1]]

B = [[0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0],
    [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0]]

match, w = greedy_matrix(A,B)

print(match)
print(w)
