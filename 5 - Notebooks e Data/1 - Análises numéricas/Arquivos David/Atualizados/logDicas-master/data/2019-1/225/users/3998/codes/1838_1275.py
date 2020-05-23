from numpy import *
from numpy.linalg import *

m= array(eval(input(": ")))

v =zeros (shape(m)[0], dtype= int)
for i in range(shape(m)[0]):
	v[i]= sum(m[i,:])
print(v)