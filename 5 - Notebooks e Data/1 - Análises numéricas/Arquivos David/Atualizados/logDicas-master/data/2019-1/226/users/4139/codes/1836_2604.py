from numpy import*
from numpy.linalg import*

y = array(eval(input("eng. mec: ")))

for i in range(shape(y)[0]):
	print(max(y[i]))