from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data = input("Informe o Mes dd/mm/aaaa:")

dia = (data[0:2])
mes = (data[2:4])
ano = (data[4:8])

mes = vet_mes[int(mes) - 1]

print(dia + " de " + mes + " de " + ano)
		