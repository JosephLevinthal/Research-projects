from numpy import*
from numpy.linalg import*

x = array(eval(input("Entrada:")))

for i in range(shape(x)[0]):
	print(max(x[i]))