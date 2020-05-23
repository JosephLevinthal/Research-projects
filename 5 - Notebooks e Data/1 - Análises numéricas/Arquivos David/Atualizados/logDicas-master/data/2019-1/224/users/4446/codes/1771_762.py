from numpy import *

data=input("digite a data: ")
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
dia= data[ :2]
mes= int(data[2:4])
ano= data[4: ]

print(dia,"de",vet_mes[mes-1],"de",ano)
	