from blocks import *

def minMatchingGreedy(X, Y):
    n = len(X)
    m = len(Y)
    Match = []
    w = 0
    for i in range(min(n,m)-1):
        Match.append((i,i))
        w += X[i]/Y[i]
    if n>m:
        for i in range(-1,n-m):
            Match.append((m+i,m-1))
            w += X[m+i]/Y[m-1]
    else:
        for i in range(-1,m-n):
            Match.append((n-1,n+i))
            w += X[n-1]/Y[n+i]
    return Match, w

'''A = [0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1]
B = [0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0]
M,  = minMatchingGreedy(A,B)
print(w)
print(M)'''
