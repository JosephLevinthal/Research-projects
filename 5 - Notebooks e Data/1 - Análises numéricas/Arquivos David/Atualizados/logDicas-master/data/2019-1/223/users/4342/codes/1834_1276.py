from numpy import *
from numpy.linalg import * 

quadro = array(eval(input("quadro:")))
vet = zeros(7,dtype = int)

for i in range (7):
	vet[i] = sum(quadro[:,i])
for i in range (7):
	if vet[i] == max(vet):
		print(i+1)

	
