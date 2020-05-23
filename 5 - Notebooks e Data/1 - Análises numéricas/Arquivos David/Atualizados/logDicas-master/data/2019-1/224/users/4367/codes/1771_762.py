from numpy import *
# Vetor contendo o nome dos meses do ano
vm = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
d=input("digite a data:")
n=int(d[2:4])
print(d[:2], "de", vm[n-1], "de", d[4:8])