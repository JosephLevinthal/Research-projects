from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite as horas: ")))


b = zeros((7), dtype= int)

for i in range(7):
	b[i] = sum(v[:,i])
	
	if	(b[i] == max(b)):
			a = i + 1

print(a)