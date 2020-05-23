from numpy import*
from numpy import *
vet1 = array(eval(input("Digite um vetor para Eusapio: ")))
vet2 = array(eval(input("Digite um vetor para Barsanulfo: ")))
pont1 = 0
pont2 = 0

i = 0

while (i < size(vet1)):
	if (vet1[i] == 11): #pedra
		if (vet2[i] == 22):#papel
			pont2 += 1
		elif (vet2[i] == 33):#tesoura
			pont1 += 1
	if (vet1[i] == 22):
		if (vet2[i] == 11):
			pont1 += 1
		elif (vet2[i] == 33):
			pont2 += 1
	if (vet1[i] == 33):
		if (vet2[i] == 11):
			pont2 += 1
		elif (vet2[i] == 22):
			pont1 += 1
	i += 1
	
print(size(vet1))
if (pont1 > pont2):
	print("EUSAPIA")
if (pont1 < pont2):
	print("BARSANULFO")
if (pont1 == pont2):
	print("EMPATE")