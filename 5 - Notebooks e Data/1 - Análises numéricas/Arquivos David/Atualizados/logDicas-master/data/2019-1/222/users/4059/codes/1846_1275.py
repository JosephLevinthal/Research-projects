from numpy import *
from numpy.linalg import *
m=array(eval(input("Matriz: ")))
l=shape(m)[0]
z=zeros(l, dtype=int)
for i in range(l):
	for j in range(7):
		z[i]=z[i]+m[i,j]
print(z)

