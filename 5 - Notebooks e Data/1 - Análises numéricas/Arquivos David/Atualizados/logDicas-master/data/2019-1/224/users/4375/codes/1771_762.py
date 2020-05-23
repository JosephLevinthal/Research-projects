from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
date=input("write date: ")
n=int(date[2:4])
print(date[:2],"de",vet_mes[n-1],"de", date[4:8])