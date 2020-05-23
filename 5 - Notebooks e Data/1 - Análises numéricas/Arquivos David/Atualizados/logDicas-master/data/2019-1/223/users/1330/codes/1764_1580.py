from numpy import *

vet1 = array(eval(input()))
vet2 = array(eval(input()))

falta = 0
passou = 0
reprovou = 0
soma = 0
i = 0
maior = max(vet1)
while(i<size(vet1)):
	if(vet1[i]==(-1)):
		falta = falta + 1	
	elif(vet1[i]>=6):
		passou = passou +1
		soma = soma + vet1[i]
	elif(vet1[i]<6):
		reprovou = reprovou + 1
		soma = soma + vet1[i]
	if(vet1[i]==maior):
		maior = vet2[i]
	
	i = i + 1

print(falta)
print(passou)
print(reprovou)
print(round(soma/ (reprovou+passou),2))
print(maior)