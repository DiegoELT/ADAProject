from blocks import *
import sys, math
import time

minMatch = []
accumX = []
accumY = []

def group(X,Y,i,j):
	Min = math.inf
	Match = []
	for k in range(i):
		tmatch = [(p,j) for p in range(k+1,i+1)]
		accum = (accumX[i] - accumX[k]) / Y[j]
		match, pmin = minMatchingMemoization(X,Y,k,j-1)
		if(Min > accum+pmin):
			Min = accum+pmin
			Match = tmatch+match
	return Match, Min
		
def division(X,Y,i,j):
	Min = math.inf
	Match = []
	for k in range(j):
		accum = X[i] / (accumY[j] - accumY[k])
		match, pmin = minMatchingMemoization(X,Y,i-1,k)
		if(Min > accum+pmin):
			tmatch = [(i,p) for p in range(k+1,j+1)]
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
		minMatch[i][j][1] = X[i] / accumY[j]
		return minMatch[i][j][0], minMatch[i][j][1]
	if(i>0 and j==0):
		match = [(p,j) for p in range(i+1)]
		minMatch[i][j][0] = match
		minMatch[i][j][1] = accumX[i] / Y[j]
		return minMatch[i][j][0], minMatch[i][j][1]
	MatchG, MinG = group(X,Y,i,j)
	MatchD, MinD = division(X,Y,i,j)
	if(MinG > MinD):
		minMatch[i][j][0] = MatchD
		minMatch[i][j][1] = MinD
		return minMatch[i][j][0], minMatch[i][j][1]
	minMatch[i][j][0] = MatchG
	minMatch[i][j][1] = MinG
	return minMatch[i][j][0], minMatch[i][j][1]

def minMatchingM(X,Y):
	global minMatch
	minMatch = [[[[],math.inf] for s in range(len(Y))] for l in range(len(X))]
	accumX.append(X[0])
	accumY.append(Y[0])
	for i in range(1,len(X)):
		accumX.append(accumX[i-1] + X[i])
	for j in range(1,len(Y)):
		accumY.append(accumY[j-1] + Y[j])
	return minMatchingMemoization(X,Y,len(X)-1,len(Y)-1)
	
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
print("Tiempo de ejecucion:",time.time()-start_time)
print(w)
print(sorted(M))
'''
