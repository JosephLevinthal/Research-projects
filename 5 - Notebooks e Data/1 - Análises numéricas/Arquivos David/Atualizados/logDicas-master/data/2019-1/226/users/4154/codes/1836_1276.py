from numpy import *
from numpy.linalg import *
a = array(eval(input()))
b = zeros(7, dtype=int)
for i in range(7):
	b[i] = sum(a[:,i])
for i in range(7):
	if max(b) == sum(a[:,i]):
		print(i+1)