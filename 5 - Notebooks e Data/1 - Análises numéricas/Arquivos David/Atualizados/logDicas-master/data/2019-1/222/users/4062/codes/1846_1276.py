from numpy import *
from numpy.linalg import *
m=array(eval(input("Matriz: ")))
l=shape(m)[0]
z=zeros(l, dtype=int)
for j in range(7):
	z[j]=sum(m[:,j])
for p in range(7):
	if z[p]==max(z):
		print(p+1)

