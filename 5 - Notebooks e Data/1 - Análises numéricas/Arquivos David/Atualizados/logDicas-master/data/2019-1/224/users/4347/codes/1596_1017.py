# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
t1= radians(float(input("Latitude de p1: ")))
g1= radians(float(input("Latitude de g1: ")))
t2= radians(float(input ("Latitude de t2: ")))
g2= radians(float(input("Latitude de g2: ")))
raio= 6371.01
distancia= raio*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(round(distancia, 2))
