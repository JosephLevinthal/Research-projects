# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import radians
from math import sin
from math import cos
from math import acos

t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("Longitude de P1: "))) 
t2 = radians(float(input("Latitude de P2: ")))
g2 = radians(float(input("Longitude de P2: ")))
R =float(6371.01)
A = (sin(t1) * sin(t2))
B = (cos(t1) * cos(t2))
C = (cos(g1-g2))
D = A + B * C
E = acos(D)

d = R * E
print(round(d, 2))


