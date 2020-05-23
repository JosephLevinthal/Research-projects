from math import *
H = float(input("Altura do tanque: "))
h = float(input("Nivel de Combustivel do tanque: "))
r = float(input("Raio dos bojos semiesfericos inferior e superior: "))

print("Entradas:",H, ",",h, ",",r)

if(H < 0) or (h < 0) or (r < 0) or (H < h) or (H < (2*r)):
	print("Entradas invalidas")

elif (H < 0):
		volume = ((1/3) * pi * h ** 2 * (3 * r - H)) * 1000
		print("Volume:",round(volume,3),"litros")
		
elif (h < H - r):
		volume = ((2/3) * pi * raio ** 3 + pi * raio ** 2 * (nivelH - raio)) * 1000
		print("Volume:",round(volume,3),"litros")
		
elif (H <= H):
		volume = ((4/3) * pi * r ** 3 + pi * raio ** 2 * (H - 2 * r) - (1/3) * pi * (H - h) ** 2 * (3 * raio - alturaH + nivelH)) * 1000
		print("Volume:",round(volume,3),"litros")
