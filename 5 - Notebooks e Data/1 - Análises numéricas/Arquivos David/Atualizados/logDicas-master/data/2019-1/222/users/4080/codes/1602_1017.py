# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("longitude de p1: ")))
t2 = radians(float(input("Latitude de P2: ")))
g2 = radians(float(input("longitude de p2: ")))
R = 6371.01
D = R*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1 - g2))
print(round(D ,2))