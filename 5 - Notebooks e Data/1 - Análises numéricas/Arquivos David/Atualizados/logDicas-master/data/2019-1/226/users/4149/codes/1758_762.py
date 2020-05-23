from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data=input("entre com afdfaz: ")
dd=data[:2]
mm=data[2:4]
aaa=data[4:]

t=int(mm)-1

print(dd,"de",vet_mes[t],"de",aaa)
