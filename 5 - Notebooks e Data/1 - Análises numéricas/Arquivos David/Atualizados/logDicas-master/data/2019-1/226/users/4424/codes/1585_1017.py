# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *

t1=float(input("digite a latitude 1"))
g1=float(input("digite a longitude do ponto 1"))
t2=float(input("digite a latitude 2"))
g2 =float(input("digite a longitude do ponto 2"))

te1=radians(t1)
ge1=radians(g1)
te2=radians(t2)
ge2=radians(g2)

R=6371.01

d = R*acos(sin(te1)*sin(te2)+ cos(te1)*cos(te2)*cos(ge1-ge2))

print(round(d,2))