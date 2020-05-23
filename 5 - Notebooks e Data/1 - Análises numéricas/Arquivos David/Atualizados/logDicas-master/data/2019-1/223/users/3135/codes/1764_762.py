from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("Informe a data: ")
dia=data[:2]
mes=int(data[2:4])
ano=data[4:]
if( mes>=1 and mes<=12):
	m=mes-1
	vet=vet_mes[m]
print(dia, "de",  vet,  "de",  ano)