from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
x = input("digite a data: ")

dd = x[0:2]
mm = x[2:4]
an = x[4:8]
mes = vet_mes[int(mm)-1]

print(dd, "de", mes, "de", an)