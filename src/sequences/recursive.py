from blocks import *
import sys, math
import time

def group(X,Y,i,j):
	Min = math.inf
	Match = []
	for k in range(i):
		tmatch = [(p,j) for p in range(k+1,i+1)]
		accum = sum(X[k+1:i+1])/Y[j]
		match, pmin = minMatchingRecursive(X,Y,k,j-1)
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
		match, pmin = minMatchingRecursive(X,Y,i-1,k)
		if(Min > accum+pmin):
			Min = accum+pmin
			Match = tmatch+match
	return Match, Min

def minMatchingRecursive(X,Y,i,j):
	if(i==0 and j==0):
		return [(i,j)], X[i]/Y[j]
	if(i==0 and j>0):
		match = [(i,p) for p in range(j+1)]
		return match, X[i]/sum(Y[:j+1])
	if(i>0 and j==0):
		match = [(p,j) for p in range(i+1)]
		return match, sum(X[:i+1])/Y[j]
	MatchG, MinG = group(X,Y,i,j)
	MatchD, MinD = division(X,Y,i,j)
	if(MinG > MinD):
		return MatchD, MinD
	return MatchG, MinG
	

'''A = [0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1]
B = [0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0]
X = getBlocks(A,len(A))
Y = getBlocks(B,len(B))
print(X)
print(Y)
start_time = time.time()
M, w = minMatchingRecursive(X,Y,len(X)-1,len(Y)-1)
print(time.time()-start_time)
print(w)
print(sorted(M))'''
