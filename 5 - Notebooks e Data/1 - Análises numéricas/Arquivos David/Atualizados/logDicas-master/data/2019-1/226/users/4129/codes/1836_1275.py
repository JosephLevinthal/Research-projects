from numpy import*
from numpy.linalg import*

f = array(eval(input("Entrada:")))

dias = zeros(shape(f)[0], dtype=int)
for i in range(shape(f)[0]):
	dias[i]= sum(f[i,:])

print(dias)
	