from numpy import*
from numpy.linalg import*
n= array(eval(input("NUMERO DE FUNCIONARIOS: ")))
#print(shape(n)[1])
for x in range(shape(n)[0]):
	k = max(n[x,:])
	print(k)