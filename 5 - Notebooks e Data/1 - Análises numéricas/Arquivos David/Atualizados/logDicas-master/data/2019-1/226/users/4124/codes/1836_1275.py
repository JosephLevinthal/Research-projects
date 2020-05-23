from numpy import *
from numpy.linalg import *
v = array(eval(input("Horas de trabalho: ")))
a = shape(v)[0]
n = zeros(a, dtype = int)
#for i in range(n):
for i in range(a):
	n[i] = sum(v[i,:])
print(n)