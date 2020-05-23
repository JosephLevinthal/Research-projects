from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data=input("digite a data: ")
dd=data[0:2]
m=data[2:4]
a=data[4: ]
t=int(m)-1

print(dd ,"de" ,vet_mes[t],"de" ,a)

