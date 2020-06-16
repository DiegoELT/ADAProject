from blocks import *
import sys, math
import time

minMatch = []

def group(X,Y,i,j):
	Min = math.inf
	Match = []
	for k in range(i):
		tmatch = [(p,j) for p in range(k+1,i+1)]
		accum = sum(X[k+1:i+1])/Y[j]
		match, pmin = minMatchingMemoization(X,Y,k,j-1)
		if(Min > accum+pmin):
			Min = accum+pmin
			Match = tmatch+match
	return Match, Min
		
def division(X,Y,i,j):
	Min = math.inf
	Match = []
	for k in range(j):
		tmatch = [(i,p) for p in range(k+1,j+1)]
		accum = X[i]/sum(Y[k+1:j+1])
		match, pmin = minMatchingMemoization(X,Y,i-1,k)
		if(Min > accum+pmin):
			Min = accum+pmin
			Match = tmatch+match
	return Match, Min

def minMatchingMemoization(X,Y,i,j):
	if(minMatch[i][j][1]!=math.inf):
		return minMatch[i][j][0], minMatch[i][j][1]
	if(i==0 and j==0):
		minMatch[i][j][0] = [(i,j)]
		minMatch[i][j][1] = X[i]/Y[j]
		return minMatch[i][j][0], minMatch[i][j][1]
	if(i==0 and j>0):
		match = [(i,p) for p in range(j+1)]
		minMatch[i][j][0] = match
		minMatch[i][j][1] = X[i]/sum(Y[:j+1])
		return minMatch[i][j][0], minMatch[i][j][1]
	if(i>0 and j==0):
		match = [(p,j) for p in range(i+1)]
		minMatch[i][j][0] = match
		minMatch[i][j][1] = sum(X[:i+1])/Y[j]
		return minMatch[i][j][0], minMatch[i][j][1]
	MatchG, MinG = group(X,Y,i,j)
	MatchD, MinD = division(X,Y,i,j)
	if(MinG > MinD):
		minMatch[i][j][0] = MatchD
		minMatch[i][j][1] = MinD
		return MatchD, MinD
	minMatch[i][j][0] = MatchG
	minMatch[i][j][1] = MinG
	return MatchG, MinG


'''if(len(sys.argv) > 0):
	if(sys.argv[1] == '0'):
		filename_cadena_a = str(input("Cadena A: "))
		filename_cadena_b = str(input("Cadena B: "))

		with open(filename_cadena_a) as a:
			A = [int(char) for char in a.readline()]

		with open(filename_cadena_b) as b:
			B = [int(char) for char in b.readline()]

	elif(sys.argv[1] == '1'):
		A = [int(bit) for bit in str(input("Arreglo A: "))]
		B = [int(bit) for bit in str(input("Arreglo B: "))]

	else:
		A = [0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0]
		B = [0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0]
else:
	A = [0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0]
	B = [0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0]

X = getBlocks(A,len(A))
Y = getBlocks(B,len(B))
minMatch = [[[[],math.inf] for j in range(len(Y))] for i in range(len(X))]
print(X)
print(Y)
start_time = time.time()
M, w = minMatchingMemoization(X,Y,len(X)-1,len(Y)-1)
print(time.time()-start_time)
print(w)
print(sorted(M))
'''