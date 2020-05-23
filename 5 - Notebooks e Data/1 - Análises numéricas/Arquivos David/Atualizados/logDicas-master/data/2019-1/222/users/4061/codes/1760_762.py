from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data = input("digite data: ")
mes = int(data[2:4])

print(data[0:2], "de" ,vet_mes[mes-1], "de" ,data[4:])

