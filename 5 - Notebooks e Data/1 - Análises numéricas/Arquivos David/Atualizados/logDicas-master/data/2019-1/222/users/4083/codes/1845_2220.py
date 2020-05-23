from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite a matriz: ")))
a = shape(v)[0]
b = 0
for i in range(a):
	b = max(v[i,:])
	print(b)