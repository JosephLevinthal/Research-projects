from numpy import *
# Vetor contendo o nome dos meses do ano
n = str(input("digite: "))
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

dia = (n[0:2])
m = int(n[2:4])
ano = (n[4:])
mes = vet_mes[m - 1]
print(dia,"de",mes,"de",ano)