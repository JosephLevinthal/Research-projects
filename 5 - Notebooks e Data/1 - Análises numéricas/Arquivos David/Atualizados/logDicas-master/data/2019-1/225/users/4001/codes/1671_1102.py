# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
H = float(input("Altura total do tanque: "))
h = float(input("Nivel de combustivel no tanque: "))
r = float(input("Raio dos bojos: "))
# Saidas pt. 1
print("Entradas: ", H, ",", h, ",", r)
from math import*
# Condicoes
if (H <= 0) or (h <= 0) or (r <= 0) or (H <= h) or (H <= 2*r):
	print("Entradas invalidas")
elif (h == r):
	V = ((4/3 * pi * r ** 3)/2) * 1000
	V2 = round(V, 3)
	print("Volume : ", V2, "litros")
elif (h < r):
	V = (pi / 3 * h ** 2 * (3 * r - H)) * 1000
	V2 = round(V, 3)
	print("Volume : ", V2, "litros")
elif (h == H - r):
	V = ((pi * r**2 * (H - 2 * r)) + (4/3 * pi * r ** 3)/2) * 1000
	V2 = round(V, 3)
	print("Volume: ", V2, "litros")
elif (h < H - r) and (h > r):
	V = (((4/3 * pi * r ** 3)/2) + (pi * r**2 * (h - r))) * 1000
	V2 = round(V, 3)
	print("Volume: ", V2, "litros")
elif (h > H - r):
	V = (4/3 * pi * r ** 3 + (pi * r**2 * (H - 2 * r)) - (pi / 3 * H ** 2 * (3 * r - H))) * 1000
	V2 = round(V, 3)
	print("Volume: ", V2, "litros")

	




		
