# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

import math

t1 = math.radians(float(input("Latitude de P1: ")))
g1 = math.radians(float(input("Longitude de P1: ")))
t2 = math.radians(float(input("Latitude de P2: ")))
g2 = math.radians(float(input("Longitude de P2: ")))

d = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print(round(d, 2))