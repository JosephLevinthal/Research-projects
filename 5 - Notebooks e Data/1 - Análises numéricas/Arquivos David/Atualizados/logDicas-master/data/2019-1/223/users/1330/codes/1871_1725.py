from numpy import *
from numpy.linalg import *

m = array(eval(input()))
b = 0
for i in shape(m):
	if ([i]== "B"):
		b = b + 1
	print(b)