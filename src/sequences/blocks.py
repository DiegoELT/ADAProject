def getBlocks(A, p):
    i = 0
    X = []
    while i< p:
        tmp = 0
        while i<p and  A[i]==0:
            i += 1
        while i<p and  A[i]==1:
            i += 1
            tmp += 1
        if tmp!=0:
            X.append(tmp)
    return X

