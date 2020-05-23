from numpy import *
from numpy.linalg import *

vet = array(eval(input("insira a matriz:")))

x = shape(vet)[0]

total = zeros(shape(vet)[0],dtype = int)
for i in range(shape(vet)[0]):
	total[i] = sum(vet[:,i])
	
for j in range(size(total)):
	if(total[j] == max(total)):
		print(j + 1)