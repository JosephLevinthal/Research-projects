from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("dia,mes e ano:")
mes = int(data[2:4])
dia = data[:2]
ano = data[4:]
if(mes >= 1 and mes <= 12):
	mess = mes -1
	mes1 = vet_mes[mess]
print(dia,"de",mes1,"de",ano)