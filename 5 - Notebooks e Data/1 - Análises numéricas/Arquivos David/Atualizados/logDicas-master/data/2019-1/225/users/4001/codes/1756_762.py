from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
v = input("Data: ")
d = v[0:2]
m = v[2:4]
a = v[4:]
t = vet_mes[int(v[2:4]) - 1]

print(d + " de " + t + " de " + a)