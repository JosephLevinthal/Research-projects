from numpy import*
vet1 = array(eval(input("Insira um vetor de danos: \n")))

i = 0
ataque = 0
peso = 1
acum_danos = 0
while(i < size(vet1)):
		ataque = vet1[i] * peso
		acum_danos = acum_danos + ataque
		peso = peso + 1
		i = i + 1
print(acum_danos)	