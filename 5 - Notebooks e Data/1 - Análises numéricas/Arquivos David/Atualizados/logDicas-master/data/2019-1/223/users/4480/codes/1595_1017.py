# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
t1 = radians(float(input("")))
g1 = radians(float(input("")))
t2 = radians(float(input("")))
g2 = radians(float(input("")))

d = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(round(d, 2))