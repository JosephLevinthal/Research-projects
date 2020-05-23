# Teste seu codigo aos poucos.
from math import*
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
t1 = radians(float(input("latitude de p1")))
g1 = radians(float(input("longitude de p1")))
t2 = radians(float(input("latitudede p2")))
g2 = radians(float(input("longitude de p2")))
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
R = 6371.01
d = R*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))



print (round(d, 2))
