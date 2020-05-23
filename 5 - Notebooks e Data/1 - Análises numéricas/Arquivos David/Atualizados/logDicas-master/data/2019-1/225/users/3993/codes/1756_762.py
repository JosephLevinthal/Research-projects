from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data = input("Data: ")
dia = data[0:2]
mes = ""
ano = data [4:]

i = 0
while (i <= 11):
	if ((int(data[2:4]) - 1) == i):
		mes = vet_mes[i]
	i += 1
print(str(dia) + " de " + mes + " de " + str(ano))

