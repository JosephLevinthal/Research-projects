from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite as notas: ")))
a = shape(v)[0]

b = 0

for i in range(a):
	b = b + min(v[i,:])
	
z = b/a
print(round(z, 2))