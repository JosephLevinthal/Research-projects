from numpy import *
from numpy.linalg import *

vet = array(eval(input("insira a matriz:")))

for i in range(shape(vet)[0]):
	print(max(vet[i,:]))
	