from numpy import*
from numpy.linalg import*
x = array(eval(input("digite a matriz: ")))
k = shape(x)[0]
v = zeros(k, dtype = float)
a = 0
for i in range(shape(x)[0]):
	for j in range(shape(x)[0]):
		if (i>j):
			v[a]= x[i,j]
			a = a + 1
l = sum(v)/size(v)
print(round(l,2))