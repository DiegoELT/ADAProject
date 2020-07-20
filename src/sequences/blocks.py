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

def getBase(A):
  flag = False # Checking if I am reading ones
  block_starts = []

  for i in range(len(A)):
    if (flag == False and A[i] == 1):
      flag = True
      block_starts.append(i)
    elif(flag == True and A[i] == 0):
      flag = False
  
  return block_starts
