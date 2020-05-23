from numpy import *
from numpy.linalg import *
a = array(eval(input("digite: ")))
c = shape(a)[1]
b = zeros(c,dtype=int)
for j in range(size(b)):
	b[j]= sum(a[:,j])
for j in range(size(b)):
	if (b[j]==max(b)):
		x= j + 1
		print(x)