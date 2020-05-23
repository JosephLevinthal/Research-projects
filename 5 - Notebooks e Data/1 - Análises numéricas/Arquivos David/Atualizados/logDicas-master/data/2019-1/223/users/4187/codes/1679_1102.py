from math import *
altanque = float(input("Altura do tanque: "))
nivelH = float(input("Nivel de Combustivel do tanque: "))
raio = float(input("Raio dos bojos semiesfericos inferior e superior: "))

print("Entradas:", altanque, ",", nivelH, ",", raio)

if(altanque < 0) or (nivelH < 0) or (raio < 0) or (altanque < nivelH) or (altanque < (2*raio)):
	print("Entradas invalidas")

elif (nivelH < 0):
		volume = ((1/3) * pi * nivelH ** 2 * (3 * raio - nivelH)) * 1000
		print("Volume:",round(volume,3),"litros")
		
elif (nivelH < altanque - raio):
		volume = ((2/3) * pi * raio ** 3 + pi * raio ** 2 * (nivelH - raio)) * 1000
		print("Volume:",round(volume,3),"litros")
		
elif (nivelH <= altanque):
		volume = ((4/3) * pi * raio ** 3 + pi * raio ** 2 * (altanque - 2 * raio) - (1/3) * pi * (altanque - nivelH) ** 2 * (3 * raio - alturaH + nivelH)) * 1000
		print("Volume:",round(volume,3),"litros")