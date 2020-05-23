from numpy import *
from numpy.linalg import *
a = array(eval(input()))
b = zeros(shape(a)[0], dtype=int)
for i in range(shape(a)[0]):
	b[i] = sum(a[i,:])
print(b)