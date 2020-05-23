from numpy import*
from numpy.linalg import*

x = array(eval(input("Matriz:")))

soma = 0
acumula = 0
p = 0
for i in range(shape(x)[0]):
	for j in range(shape(x)[1]):
		if i == j :
			p = p + 1
		else:
			soma = soma + x[i,j]
			acumula = acumula + 1
print (round(soma/acumula, 2))
			
	
	