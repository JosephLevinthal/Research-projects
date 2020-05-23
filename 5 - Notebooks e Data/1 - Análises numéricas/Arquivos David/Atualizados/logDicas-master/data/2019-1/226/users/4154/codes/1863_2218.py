from numpy import *
from numpy.linalg import *
a = array(eval(input()))
b = 0
for i in range(size(a[1])):
	for j in range(size(a[1])):
		if i < j:
			b += a[i,j]
print(round(b,2))