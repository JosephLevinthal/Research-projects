from numpy import *
data = str(input("data:"))
# Vetor contendo o nome dos meses do ano
mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
dia=(data[0:2])
m=int(data[2:4])
ano=data[4:]
nm=mes[m-1]
print(dia+" "+"de"+" "+nm+" "+"de"+" "+ano)