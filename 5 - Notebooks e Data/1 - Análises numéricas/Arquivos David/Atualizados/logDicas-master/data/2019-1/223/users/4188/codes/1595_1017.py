# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *

t1 = radians(float(input("Latitude de P1: "))) 
g1 = radians(float(input("Longitute de P2: ")))

t2 = radians(float(input("Latitude de G1: ")))
g2 = radians(float(input("logintude de G2: ")))

T=6371

d = T * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))
print(round(d,2))

 
