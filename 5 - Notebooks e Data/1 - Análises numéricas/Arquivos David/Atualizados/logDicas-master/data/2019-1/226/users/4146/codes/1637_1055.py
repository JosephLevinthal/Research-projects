from math import *

v0 = float(input("Velocidade inicial: "))
a = float(input("Angulo: "))
D = float(input("Distancia: "))
g = 9.8
b = radians(a)

R = (v0 ** 2) * (sin(2*b))/g

if (D - R <= 0.1):
	mensagem = "sim"
else:
	mensagem = "nao"

print(mensagem)	



