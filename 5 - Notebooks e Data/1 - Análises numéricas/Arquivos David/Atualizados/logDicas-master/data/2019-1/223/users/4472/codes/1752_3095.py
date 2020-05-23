from math import *

partida = int(input("Resultado da Partida: "))

V = 3
#vitoria = 3
#empate = 2
#derrota = 1
cont = cont + 1

while (partida != "X"):
	if (partida.upper() == 'V'):
		V = 3
		partida = partida + 3
		cont = cont + 1
		print (partida)
	elif (partida.upper() == 'E'):
		E = 2
		partida = partida + 2
		cont = cont + 1
		print (partida)
	elif (partida.upper() == 'D'):
		D = 1
		partida = partida + 1
		cont + 1
		print (partida)

