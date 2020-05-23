from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
a = input("dia , mes , ano")
dia = (a[:2])
mes = int(a[2:4])
ano = (a[4:])

if 1 <= mes <=12:
	mes -= 1
	b = vet_mes[mes]
print(str(dia),"de",str(b),"de",str(ano))


