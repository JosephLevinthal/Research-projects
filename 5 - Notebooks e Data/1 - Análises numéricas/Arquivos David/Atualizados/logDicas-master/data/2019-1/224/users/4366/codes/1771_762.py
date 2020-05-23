from numpy import *
# Vetor contendo o nome dos meses do ano
vm= array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
d=input("digite a data:")
c=int(d[2:4])
print(d[:2], "de",vm[c-1],"de",d[4:8])