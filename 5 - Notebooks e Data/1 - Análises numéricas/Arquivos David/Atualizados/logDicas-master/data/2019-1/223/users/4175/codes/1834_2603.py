from numpy import *
from numpy.linalg import *

x = array(eval(input()))

for i in range(shape(x)[1]):
	x[:,i] = sorted(x[:,i],reverse=True)
print(x)