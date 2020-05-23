from numpy import *
from numpy.linalg import *

m=array(eval(input("")))
v=zeros(shape(m)[0],dtype=float)
v1=zeros(shape(m)[1],dtype=float)
a=0
b=0
for i in range(size(v)):
	for j in range(7):
		v1[j]=m[i,j]
	v[i]=max(v1)
for i in range(size(v)):
	print(v[i])