from math import*
# Valor fixo
g = 9.8
# Entradas
Vo = float(input("Vo: "))
alpha = radians(float(input("Angulo: ")))
D = float(input("Distancia: "))

R = (Vo ** 2 * sin(2 * alpha))/g
# Saidas
if (abs(D - R <= 0.1 )):
	msg = "sim"
else:
	msg = "nao"
print(msg)
