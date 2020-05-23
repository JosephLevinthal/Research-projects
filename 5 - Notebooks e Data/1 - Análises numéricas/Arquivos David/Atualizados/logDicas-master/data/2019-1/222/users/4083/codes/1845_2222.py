from numpy import*
from numpy.linalg import*

n = int(input(""))
v = array(eval(input("")))
a = shape(v)[0]
b = shape(v)[1]
c = 0
d = 0
for i in range(a):
	for j in range(b):
		if (i == j):
			c = c + v[i,j]
		if	((i + j) == (n-1)):
				d = d + v[i,j]
				
h = c - d
print(h)
