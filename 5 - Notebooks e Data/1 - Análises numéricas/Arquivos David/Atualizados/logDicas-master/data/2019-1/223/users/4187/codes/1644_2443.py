from math import *

raio = float(input("Raio: "))
alturaX = float(input("Altura da Coluna de Ar: "))
opcao = int(input("Opcao desejada (1- Volume de Ar | 2- Volume do Combustivel) "))

volumeAr = ((pi * (alturaX ** 2)) * ((3 * raio) - alturaX)) / 3
volumeEsfera = (4 * pi * (raio ** 3)) / 3
volumeCombustivel = volumeEsfera - volumeAr

if opcao == 1:
	print (round(volumeAr,4))
else:
	print (round(volumeCombustivel,4))