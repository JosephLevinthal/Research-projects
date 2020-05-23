from numpy import *
from numpy.linalg import *

x = array(eval(input()))
y = zeros(x.shape[0],dtype=int)
h = 0
for i in range(x.shape[0]):
	y[i] = min(x[i,:])
	h += min(x[i,:])
print(round(sum(h)/size(y),2))