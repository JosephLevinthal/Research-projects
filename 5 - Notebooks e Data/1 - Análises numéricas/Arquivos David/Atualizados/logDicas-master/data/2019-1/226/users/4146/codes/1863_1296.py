from numpy import *
from numpy.linalg import *

producao = array([[8, 10, 16],
					 [2, 3, 5],
					 [1, 2 ,3]])

horas = array(eval(input("Horas: ")))

horas = horas.T

vet = dot(inv(producao), horas)

print("centurion: ", round(vet[0], 1))
print("tribune: ", round(vet[1], 1))
print("senator: ", round(vet[2], 1))

if(vet[0] == min(vet)):
	print("centurion")
elif(vet[1] == min(vet)):
	print("tribune")
elif(vet[2] == min(vet)):
	print("senator")