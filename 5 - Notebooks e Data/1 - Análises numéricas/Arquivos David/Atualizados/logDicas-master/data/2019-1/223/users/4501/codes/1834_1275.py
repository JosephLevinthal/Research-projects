from numpy import*
from numpy.linalg import *
a=array(eval(input("vetor: ")))
b=zeros(a.shape[0], dtype=int)
for i in range(a.shape[0]):
	b[i]=sum(a[i,:])
print(b)	