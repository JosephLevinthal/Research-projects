from numpy import *

vet1 = array(eval(input("Vetor 1: ")))
vet2 = array(eval(input("Vetor 2: ")))
n1 = 0
n2 = 0
cont = 0

while(cont < len(vet1)):
	if(vet1[cont]==11):
		if(vet2[cont]==22):
			n2 += 1
		elif(vet2[cont]==33):
			n1 += 1
	elif(vet1[cont]==22):
		if(vet2[cont]==11):
			n1 += 1
		elif(vet2[cont]==33):
			n2 += 1
	elif(vet1[cont]==33):
		if(vet2[cont]==11):
			n2 += 1
		elif(vet2[cont]==22):
			n1 += 1
	cont += 1
	
print(cont)
if(n1 == n2):
	print("EMPATE")
elif(n1 > n2):
	print("EUSAPIA")
else:
	print("BARSANULFO")