from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("digite a data: ")
n = int(data[2:4])
print(data[:2],"de",vet_mes[n-1],"de",data[4:8])