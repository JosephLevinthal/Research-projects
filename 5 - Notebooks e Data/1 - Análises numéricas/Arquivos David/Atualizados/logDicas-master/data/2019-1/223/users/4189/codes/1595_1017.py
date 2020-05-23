# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math as mt
t1 = mt.radians(float(input("Latitude de P1: ")))
g1 = mt.radians(float(input("longitude de p1: ")))
t2 = mt.radians(float(input("latitude de p2: ")))
g2 = mt.radians(float(input("longitude de p2: ")))
R = 6371.01
d = R*mt.acos(mt.sin(t1)*mt.sin(t2) + mt.cos(t1)*mt.cos(t2)*mt.cos(g1-g2))
print(round(d,2))
