from numpy import*
from numpy.linalg import*

y=array(eval(input("Digite a matriz: ")))
for x in range(shape(y)[0]):
	print(max(y[x]))
	