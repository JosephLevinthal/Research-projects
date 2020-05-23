from numpy import *
# Vetor contendo o nome dos meses do ano
vm = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("dia,mes e ano:")
dia = data[:2]
mes = int(data[2:4])
ano = data[4: ]
if(mes >= 1 and mes <= 12):
	mess = mes - 1
	mes1 = vm[mess]
	print(dia,"de",mes1,"de",ano)