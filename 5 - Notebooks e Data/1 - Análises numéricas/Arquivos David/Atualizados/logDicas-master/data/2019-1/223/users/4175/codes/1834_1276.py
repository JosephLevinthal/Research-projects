from numpy import *
from numpy.linalg import *


x = array(eval(input()))

y = shape(x)[1]
w = zeros(y,dtype=int)
for i in range (size(w)):
	w[i] = sum(x[:,i])
a = 0

for j in range(size(w)):
	if (w[j]==max(w)):
		a = j + 1
		print(a)