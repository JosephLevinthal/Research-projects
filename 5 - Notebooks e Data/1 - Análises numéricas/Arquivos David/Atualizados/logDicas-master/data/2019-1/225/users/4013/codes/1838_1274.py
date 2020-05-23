from numpy import *
N = int(input(""))
M = zeros((N,N),dtype = int)
N-=1    #n = N - 1
k =0
for i in range(N,-1,-1):
	for j in range(N,-1,-1):
		M[i][j] = i+1
		M[j][i] = i+1
print(M)