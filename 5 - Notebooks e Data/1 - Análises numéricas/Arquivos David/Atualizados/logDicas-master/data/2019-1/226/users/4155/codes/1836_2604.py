from numpy import*
from numpy.linalg import*

x = array(eval(input("v: ")))

for y in range(shape(x)[0]):
	print(max(x[y]))