from numpy import *
from numpy.linalg import *
a=array(eval(input("digite: ")))
b=0
e=0
for i in range(shape(a)[0]):
	for j in range(shape(a)[1]):
		if(i==j):
			b = a[i,j] + b
		c = shape(a)[0] - 1
		d = shape(a)[1] - 1
		if (i == i and j == d - i ):
			e = a[i,j] + e
print(b-e)
