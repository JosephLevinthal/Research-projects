from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
st=input("data desejada: ")
d=st[0:2]
me=st[2:4]
a=st[4:8]
m=vet_mes[int(me)-1]
print(d," de ",m," de ",a)