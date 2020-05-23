from numpy import *
data=input("Digite a data:ddmmaaaa ")
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
a=int(data[2:4])
mes=vet_mes[a-1]
print(data[:2],"de", mes, "de", data[-4:])
			