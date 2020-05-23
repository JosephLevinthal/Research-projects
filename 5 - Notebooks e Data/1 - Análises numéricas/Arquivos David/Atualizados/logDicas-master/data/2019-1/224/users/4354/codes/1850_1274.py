from numpy import *
from numpy.linalg import *
N = int(input('digite o numero: '))
mz = zeros((N,N),dtype = int)
for i in range(N):
	for j in range(i,N):
		mz[i,j] = i + 1
		mz[j,i] = i + 1
print(mz)