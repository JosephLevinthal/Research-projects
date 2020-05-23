from numpy import *

vet_notas=array(eval(input("digite")))
vet_freq=array(eval(input("digite")))
numero_horas=int(input('digite'))
resultado=zeros(3,dtype=int)

for i in range(size(vet_freq)):
	
	if (vet_freq[i]< 0.75 * numero_horas):
		resultado[2] = resultado[2] + 1
		
	elif(vet_notas[i]<5):
		resultado[1]=resultado[1] +1
		
	else:
		resultado[0]=resultado[0] +1
		
print(resultado)