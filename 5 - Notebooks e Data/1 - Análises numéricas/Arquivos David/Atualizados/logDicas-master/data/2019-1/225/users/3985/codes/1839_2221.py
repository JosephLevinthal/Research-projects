from numpy import*
from numpy.linalg import*

a=array(eval(input()))
s = 0

for i in range(shape(a)[0]):
	s += min(a[i,:])
d= s/shape(a)[0]
print(round(d,2))