# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
lat1 = radians(float(input("Latitude de P1: ")))
long1 = radians(float(input("Latitude de P1: ")))
lat2 = radians(float(input("Latitude de P2: ")))
long2 = radians(float(input("Latitude de P2: ")))
R = 6371.01
d = R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))
print(round(d, 2))