from numpy import *
from numpy.linalg import *

x=array(eval(input(":")))
vet=zeros(shape(x)[1],dtype=int)

for j in range(7):
	for i in range(shape(x)[0]):
		  vet[j]+=x[i,j]
		  
for i in range(size(vet)):
	if(vet[i]==max(vet)):
		  print(i+1)