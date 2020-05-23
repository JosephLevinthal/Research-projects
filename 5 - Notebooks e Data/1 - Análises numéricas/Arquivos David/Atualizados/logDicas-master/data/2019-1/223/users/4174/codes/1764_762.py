from numpy import *
# Vetor contendo o nome dos meses do ano
v = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("dia,mes e ano:")

dia = data[:2]
mes = int(data[2:4])
ano = data[4:]

if( 1 <= mes <= 12):
	mes = mes - 1
	mes1 = v[mes]
print(dia,"de",mes1,"de",ano)