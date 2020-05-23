# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
t1 =radians(float(input("Latitude do Ponto 1: ")))
g1 =radians(float(input("Longitude do Ponto 1: ")))
t2 =radians(float(input("Latitude do Ponto 2: ")))
g2 =radians(float(input("Longitude do Ponto 2: ")))
R=6371.01
d = R * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))

print(round(d, 2))