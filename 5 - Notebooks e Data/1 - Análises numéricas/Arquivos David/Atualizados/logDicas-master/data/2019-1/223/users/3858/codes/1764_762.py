from numpy import *
data = input()
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
dia = int(data[0:2])
mes = int(data[2:4])
ano = int(data[4:8])
mesnovo = mes -1


print(dia,"de",vet_mes[mesnovo],"de",ano)