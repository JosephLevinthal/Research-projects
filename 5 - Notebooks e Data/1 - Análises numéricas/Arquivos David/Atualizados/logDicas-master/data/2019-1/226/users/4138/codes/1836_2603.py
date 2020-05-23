from numpy import *
from numpy.linalg import *

vet = array(eval(input("insira a matriz:")))
vet = vet


for i in range(4):
	vet[:,i] = sorted(vet[:,i],reverse = True)
print(vet)