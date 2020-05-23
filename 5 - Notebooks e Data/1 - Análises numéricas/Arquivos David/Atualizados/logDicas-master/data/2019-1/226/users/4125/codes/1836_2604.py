from numpy import*
from numpy.linalg import*

x = array(eval(input("digite a matriz: ")))
for i in range(shape(x)[0]):
	print(max(x[i]))