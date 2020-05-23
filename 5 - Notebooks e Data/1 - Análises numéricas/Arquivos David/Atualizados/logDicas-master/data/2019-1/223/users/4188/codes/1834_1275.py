from numpy import *
from numpy.linalg import *
a = array(eval(input("digite: ")))
c = shape(a)[0]
b = zeros(c, dtype=int)
for i in range(c):
	b[i] = sum(a[i,:])
print(b)