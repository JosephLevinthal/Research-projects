# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

#Ler os dados de entrada
from math import*
t1 = radians(float(input("Latitude de P1: ")))
g1 = radians(float(input("Longitude de P1: ")))
t2 = radians(float(input("Latitude de P2: ")))
g2 = radians(float(input("Longitude de P2: ")))

#calcular a distancia
R=6371.01 #está em km o raio médio da Terra
d=R*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))

#imprimir a distancia
print(round(d,2))