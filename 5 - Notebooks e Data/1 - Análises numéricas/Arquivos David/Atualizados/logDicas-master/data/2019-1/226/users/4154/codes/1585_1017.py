# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
lata = radians(float(input("Latitude de P1: ")))
longa = radians(float(input("Longitude de P1: ")))
latb = radians(float(input("Latitude de P2: ")))
longb = radians(float(input("Longitude de P2: ")))
R = 6371.01

d = R*acos((sin(lata)*sin(latb)+cos(lata)*cos(latb)*cos(longa-longb)))
print(round(d,2))