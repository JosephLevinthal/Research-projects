from numpy import *
from numpy.linalg import *

mat=array(eval(input("digite: ")))
x=shape(mat)[0]
vet=zeros(x, dtype=int)
for i in range(x):
	func=sum(mat[i,:])
	vet[i]=func
	func=0
print(vet)