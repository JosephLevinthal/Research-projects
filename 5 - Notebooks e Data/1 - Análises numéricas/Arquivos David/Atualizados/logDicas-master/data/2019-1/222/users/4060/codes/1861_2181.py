from numpy import*
from numpy.linalg import*

matriz=array(eval(input("matrix: ")))
num=shape(matriz)[0]
zeros=zeros((num**2-num), dtype=float)
k=0
for i in range(num):
	for j in range(num):
		if((i+j)!=(num-1)):
			zeros[k]=matriz[i,j]
			k=k+1
print(round(min(zeros), 2))