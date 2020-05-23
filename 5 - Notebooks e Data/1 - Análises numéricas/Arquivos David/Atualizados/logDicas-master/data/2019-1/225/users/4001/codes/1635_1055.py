# Valores fixos
g = 9.8
# Entradas
from math import*
Vo = float(input("Velocidade inicial: "))
alpha = radians(float(input("Angulo alpha: ")))
D = float(input("Distania D: "))
R = ((Vo) ** 2 * sin(2 * alpha))/g

if( abs(D - R)<= 0.1):
	msg = "sim"
else:
	msg = "nao"
# Saida
print(msg)