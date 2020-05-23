from numpy import*
from numpy.linalg import*

matriz = array(eval(input("Leia: ")))

s=0

for i in range(shape(matriz)[0]):
	s = s + min(matriz[i,:])
	
print(round(s/shape(matriz)[0],2))