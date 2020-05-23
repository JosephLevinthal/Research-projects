from numpy import *
# Vetor contendo o nome dos meses do ano
v = input("DD MM AAAA: ")

vm= array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])


p = int(v[2:4])

d = v[0:2]
m = vm[p-1]
a = int(v[4:8])

print(d, "de", m, "de", a)