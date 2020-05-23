from numpy import *
peso = array(eval(input("peso:")))
altura = array(eval(input("altura:")))

vet = zeros(size(peso))

for i in range(size(peso)):
	vet[i] = round(peso[i] / (altura[i])**2,2)
print(vet)
print("O MAIOR IMC DA TURMA EH:",max(vet))

if(max(vet) < 17):
	print("MUITO ABAIXO DO PESO")
elif(max(vet) >= 17 and max(vet) <= 18.49):
	print("ABAIXO DO PESO")
elif(max(vet) >= 18.5 and max(vet) <= 24.99):
	print("PESO NORMAL")
elif(max(vet) >= 25 and max(vet) <= 29.99):
	print("ACIMA DO PESO")
elif(max(vet) >= 30 and max(vet) <= 34.99):
	print("OBESIDADE")
elif(max(vet) >= 35 and max(vet) <= 39.99):
	print("OBESIDADE SEVERA")
elif(max(vet) >= 40):
	print("OBESIDADE MORBIDA")

		

