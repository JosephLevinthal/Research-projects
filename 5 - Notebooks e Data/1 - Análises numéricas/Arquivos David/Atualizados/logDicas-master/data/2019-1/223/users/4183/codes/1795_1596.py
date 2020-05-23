from numpy import *
v = array(eval(input("Digite o vetor de notas: ")))
soma = sum(v) - min(v)
tam = size(v) - 1
med = soma/tam
print(round(med,2))