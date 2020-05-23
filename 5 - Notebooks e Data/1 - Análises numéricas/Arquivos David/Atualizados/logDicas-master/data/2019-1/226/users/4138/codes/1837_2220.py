from numpy import *
from numpy.linalg import *

vet = array(eval(input("insira a entrada")))

a = shape(vet)[0]

for i in range(shape(vet)[0]):
	print(max(vet[i,:]))