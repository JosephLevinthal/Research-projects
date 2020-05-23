from numpy import *
# Vetor contendo o nome dos meses do ano
v = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])

data = input("insira a data:")
dia = data[:2]
mes = data[2:4]
ano = data[4:]

mes = int(mes)
mes1 = mes -1 



print(dia, "de", v[mes1], "de",ano)




