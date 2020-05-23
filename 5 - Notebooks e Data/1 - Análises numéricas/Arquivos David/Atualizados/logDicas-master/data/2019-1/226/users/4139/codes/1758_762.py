from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("digite dia mes ano: ")

dia = int(data[:2])
ano = int(data[4:9])
i = int(data[2:4]) -1
mes = vet_mes[i]

print(dia,"de",mes,"de",ano)