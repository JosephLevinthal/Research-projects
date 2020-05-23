from numpy import *
from numpy.linalg import *
mat=array(eval(input("digite: ")))
x=shape(mat)[1]
vet=zeros(x, dtype=int)
for j in range(x):
	func=sum(mat[:,j])
	vet[j]=func
for m in range(size(vet)):
	if (vet[m]==max(vet)):
		print(m+1)