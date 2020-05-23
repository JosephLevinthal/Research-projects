from numpy import *
from numpy.linalg import *

vet = array(eval(input("inisira a matriz:")))


total = zeros(shape(vet)[0],dtype =int)


for i in range(shape(vet)[0]):
	total[i] = sum(vet[i,:])
	
print(total)
