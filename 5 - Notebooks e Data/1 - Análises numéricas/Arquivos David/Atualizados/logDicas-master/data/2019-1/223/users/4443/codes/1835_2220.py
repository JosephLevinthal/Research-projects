from numpy import *
from numpy.linalg import *
rs = array(eval(input("Digite o salario semanal: ")))
for i in range(shape(rs)[0]):
	print(max(rs[i,:]))
			  
			  