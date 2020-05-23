from numpy import *
from numpy.linalg import *
rs = array(eval(input("digite o salario diario: ")))
for i in range(shape(rs)[0]):
	print(max(rs[i,:]))


