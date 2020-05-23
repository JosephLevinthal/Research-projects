# H é altura total do tanque
# h é o nível de combustível no tanque
# r é o raio dos bojos semiesféricos interior e superior
# V é o volume do combustível

# saída:
# Calcular volume do combustível em litros com 3 casas decimais

from math import *

alturaH = float(input("Altura do tanque: "))
nivelH = float(input("Nivel de Combustivel do tanque: "))
raio = float(input("Raio dos bojos semiesfericos inferior e superior: "))

#cilindroVolume = pi * (r ** 2) * h
#esferaVolume = (4 / 3) * pi * (r ** 3)
#calotaVolume = (pi / 3) * (h ** 2) * (3 * r - h)

print("Entradas:", alturaH, ",", nivelH, ",", raio)

if (alturaH > 0) and (nivelH > 0) and (raio > 0) and (alturaH > nivelH) and (alturaH > (2*raio)):
	
	if (nivelH < 0):
		volume = ((1/3) * pi * nivelH ** 2 * (3 * raio - NivelH)) * 1000
		print("Volume:",round(volume,3),"litros")
		
	elif (nivelH < alturaH - raio):
		volume = ((2/3) * pi * raio ** 3 + pi * raio ** 2 * (nivelH - raio)) * 1000
		print("Volume:",round(volume,3),"litros")
		
	elif (nivelH <= alturaH):
		volume = ((4/3) * pi * raio ** 3 + pi * raio ** 2 * (alturaH - 2 * raio) - (1/3) * pi * (alturaH - nivelH) ** 2 * (3 * raio - alturaH + nivelH)) * 1000
		print("Volume:",round(volume,3),"litros")
else:
	volume ="Entradas invalidas"
	print(volume)


	

	
	