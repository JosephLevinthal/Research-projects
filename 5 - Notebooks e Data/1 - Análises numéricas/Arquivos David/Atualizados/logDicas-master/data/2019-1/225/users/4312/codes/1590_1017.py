# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import*

#conversao de dados p1 para radianos
t1 = radians(float(input("latitude de p1: ")))
g1 = radians(float(input("longitude de p1: ")))

#conversao de dados de p2 para radianos
t2 = radians(float(input("latitude de p2: ")))
g2 = radians(float(input("longitude de p2: ")))

#raio da terra
r = 6371.01

#distancia d entre dois pontos
d = r * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(round(d, 2))