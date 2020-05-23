from numpy import *
# Vetor contendo o nome dos meses do ano
dd=input("data: ")
vet_mes = array(['janeiro','fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
a=int(dd[2:4])
mes=vet_mes[a-1]
print(dd[:2],"de",mes,"de",dd[4:])