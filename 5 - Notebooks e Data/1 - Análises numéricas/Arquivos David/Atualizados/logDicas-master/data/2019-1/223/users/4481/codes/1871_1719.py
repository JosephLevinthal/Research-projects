from numpy import*
from numpy.linalg import*

a = array(eval(input('digite: ')))
b= zeros(shape(a)[0], dtype=int)
c=1
for i range(shape(a)[0]):
	for j in range(shape(a)[1]):
		c=a[i,j] * c
		b[i]= c /
		
	