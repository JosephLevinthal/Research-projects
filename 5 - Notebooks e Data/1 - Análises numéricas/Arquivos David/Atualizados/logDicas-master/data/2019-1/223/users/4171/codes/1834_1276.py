from numpy import *
from numpy.linalg import*

x = array(eval(input("")))
y = shape(x)[1]
w = zeros(y, dtype = int)

for i in range(size(w)):
	w[i] = sum(x[:,i])

for i in range(size(w)):
	if w[i] == max(w):
		z = i + 1
		print(z)