from numpy import*
from numpy.linalg import*

x = array(eval(input("entrada:"))
k = shape(x)[0]
v = zeros((j), dtype = int)
a = 0
t = shape(x)[0]
for i in range(t):
	for j in range(t):
		if(i>j):
			v[a] = sum(x[i,j])
			 a = a + 1
b = sum(v)
print(round(b,2))