from numpy import *
from numpy.linalg import *
mat=int(input("digite a ordem da matriz quadrada:"))
mz=ones((mat,mat),dtype=int)
for i in range(mat):
	for j in range(i,mat):
		mz[i,j]= i +1
		mz[j,i]= i+1
print(mz)