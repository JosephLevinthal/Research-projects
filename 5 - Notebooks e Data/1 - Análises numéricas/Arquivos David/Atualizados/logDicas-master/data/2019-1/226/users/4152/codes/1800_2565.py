from numpy import *
med = array(eval(input("Vetor de Medias dos alunos: ")))
fre = array(eval(input("Vetor de Frequencias: ")))
car = int(input("Carga Horaria: "))
vet = zeros(3, dtype=int)
soma1 = 0
soma2 = 0
soma3 = 0
for i in range(size(med)):
	if med[i] >= 5 and fre[i] >= car * (75 / 100):
			soma1 = soma1 + 1
	elif med[i] < 5:
			soma2 = soma2 + 1
	elif fre[i]< car * (75 / 100):
			soma3 = soma3 + 1
vet[0] = soma1
vet[1] = soma2
vet[2]= soma3
print(vet)