from numpy import *
from numpy.linalg import *

x = array(eval(input()))
y = shape(x)[0]
w = zeros(y,dtype=int)
for i in range(y):
	w[i] = sum(x[i,:])
print(w)