from numpy import *
from numpy.linalg import *

x=array(eval(input(":")))
vet=zeros(shape(x)[0],dtype=int)

for i in range(size(vet)):
		  for j in range(7):
		  	vet[i]+=x[i,j]
print(vet)