from numpy import *

v1 = array(eval(input()))
v2 = array(eval(input()))
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
i = 0
maior = max(v1)
while v1[i] != maior:
    i = i +1
print(i+1)