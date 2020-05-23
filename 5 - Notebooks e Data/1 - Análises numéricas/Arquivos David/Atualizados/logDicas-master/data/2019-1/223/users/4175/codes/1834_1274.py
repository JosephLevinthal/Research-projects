from numpy import * 
from numpy.linalg import *

x = array(eval(input()))

y = zeros((x,x), dtype=int)
for i in range(x):
	for j in range(x):
		y[i,j] = min(i,j) +1
print(y)