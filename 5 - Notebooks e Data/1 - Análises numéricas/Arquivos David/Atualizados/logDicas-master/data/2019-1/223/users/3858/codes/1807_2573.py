from numpy import *
peso = array(eval(input()))
altura = array(eval(input()))
vet = zeros(size(peso), dtype=float)
vet2 = ''
for x in range(size(peso)):
	vet[x] = peso[x] / (altura[x] * altura[x])
	if(vet[x] == max(vet)):
		maior=x
		if(vet[maior]<17):
			vet2 ='MUITO ABAIXO DO PESO'
		elif(vet[maior]>=17 and vet[maior]<=18.49):
			vet2 ='ABAIXO DO PESO'
		elif(vet[maior]>=18.5 and vet[maior]<=24.99):
			vet2 = 'PESO NORMAL'
		elif(vet[maior]>= 25 and vet[maior]<= 29.99):
			vet2 = 'ACIMA DO PESO'
		elif(vet[maior] >= 30 and vet[maior] <= 34.99):
			vet2 = 'OBESIDADE'
		elif(vet[maior] >= 35 and vet[maior] <= 39.99):
			vet2 = 'OBESIDADE SEVERA'
		elif(vet[maior] > 40):
			vet2 = 'OBESIDADE MORBIDA'
print(vet)
print('O MAIOR IMC DA TURMA EH: ', round(vet[maior],2))
print(vet2)
