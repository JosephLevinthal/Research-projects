from numpy import*
from numpy.linalg import*

vet = array(eval(input("vetor: "))).T
mat = array([[8,10,16],
				 [2,3,5],
				 [1,2,3]])

re = 

print("centurion: ",round(vet[0,1],0))
print("tribune: ",round(vet[0,2],0))
print("senator: ",round(vet[0,3],0))
if min(vet) == vet[0,1]:
	print("centurion")
if min(vet) == vet[0,2]:
	print("tribune")
if min(vet) == vet[0,3]:
	print("senator")