from blocks import *
import sys, math
import time

minMatch = []

def minMatchingDP(X,Y):
	n = len(X)
	m = len(Y)
	minMatch[0][0] = [[(0,0)],X[0]]
	for i in range(1,n):
		#minMatch[i][0][0] = minMatch[i-1][0][0] + [(i,0)]
		minMatch[i][0][1] = minMatch[i-1][0][1] + X[i]
	minMatch[0][0][1] = Y[0]
	for j in range(1,m):
		#minMatch[0][j][0] = minMatch[0][j-1][0] + [(0,j)]
		minMatch[0][j][1] = minMatch[0][j-1][1] + Y[j]
	for i in range(1,n):
		minMatch[i][0][1] = minMatch[i][0][1] / Y[0]
	for j in range(1,m):
		minMatch[0][j][1] = X[0] / minMatch[0][j][1]
	minMatch[0][0][1] = X[0]/Y[0]
	
	for i in minMatch:
		for j in i:
			print(j, end=' ')
		print()
	
	for i in range(1,n):
		for j in range(1,m):
			for k in range(i):
				accum = sum(X[k+1:i+1])/Y[j]
				[match, pmin] = minMatch[k][j-1]
				if(minMatch[i][j][1] > accum + pmin):
					tmatch = [(p,j) for p in range(k+1,i+1)]
					#minMatch[i][j][0] = match + tmatch
					minMatch[i][j][1] = accum + pmin 
			for k in range(j):
				accum = X[i]/sum(Y[k+1:j+1])
				[match, pmin] = minMatch[i-1][k]
				if(minMatch[i][j][1] > accum + pmin):
					tmatch = [(i,p) for p in range(k+1,j+1)]
					#minMatch[i][j][0] = match + tmatch
					minMatch[i][j][1] = accum + pmin 
	for i in minMatch:
		for j in i:
			print(j, end=' ')
		print()
	
	return minMatch[n-1][m-1][0], minMatch[n-1][m-1][1]
	

A = [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1]
B = [0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0]
X = getBlocks(A,len(A))
Y = getBlocks(B,len(B))
print(X)
print(Y)
minMatch = [[[[],math.inf] for j in range(len(Y))] for i in range(len(X))]
start_time = time.time()
M, w = minMatchingDP(X,Y)
print("Tiempo de ejecucion:",time.time()-start_time)
print(w)
print(sorted(M))
