from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data = input()

d = data[:2]
m = data[2:4]
a = data[4:]

mes = int(m)

i = 0

while i != mes:
	x = vet_mes[i]
		
	i += 1

print(d, "de", x, "de", a)