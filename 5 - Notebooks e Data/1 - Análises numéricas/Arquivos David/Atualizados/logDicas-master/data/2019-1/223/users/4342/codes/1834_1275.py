from numpy import *
from numpy.linalg import *

quadro = array(eval(input("quadro de horario:")))
hora = shape(quadro)[0]
vet = zeros(hora,dtype = int)

for i in range(hora):
	vet[i] = sum(quadro[i,:])
print(vet)