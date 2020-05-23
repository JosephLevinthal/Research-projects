from numpy import*
from numpy.linalg import *
vet = array(eval(input()))
vet1 = array(vet[:,0])
vet2 = array(vet[:,1])
vet3 = array(vet[:,2])
vet4 = array(vet[:,3])
vet1 = sorted(vet1, reverse=True)
vet2 = sorted(vet2, reverse=True)
vet3 = sorted(vet3, reverse=True)
vet4 = sorted(vet4, reverse=True)
print(vet1)
#vetor = array([vet4,vet3,vet2,vet1],dtype = int)

vetor2 = zeros((4,4),dtype = int)

for j in range(0,4):
	vetor2[j,0] = vet1[j]
for j in range(0,4):
	vetor2[j,1] = vet2[j]
for j in range(0,4):
	vetor2[j,2] = vet3[j]
for j in range(0,4):
	vetor2[j,3] = vet4[j]
print(vetor2)