from numpy import *
# Vetor contendo o nome dos meses do ano
b = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
a = input("insira a string de 8 digitos: ")
dia = a[:2]
mes = a[2:4]
ano = a[4:]
i = 0
mes = int(mes)
mes1 = mes - 1
print(dia, "de", b[mes1], "de", ano)

