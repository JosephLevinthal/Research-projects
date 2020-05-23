d1 = int(input("Dado 1: "))
d2 = int(input("Dado 2: "))
rodadas = int(input("Numero de Rodadas: "))

#Saída é o tipo de ataque realizado
#	E os pontos de vida

if (d1 != 1) and (d1 != 2) and (d1 != 3) and (d1 !=4) and (d1 != 5) and (d1 != 6) and (d2 != 1) and (d2 != 2) and (d2 != 3) and (d2 !=4) and (d2 != 5) and (d2 != 6) and (rodadas < 0):
	print ("Entrada invalida")
	
if (d1 + d2 == 12):
	print ("CONSTRUCAO")
	pontosVida = d1 + d2 + 1
	print (pontosVida)
	
elif (d1 + d2 < 5):
	print ("POLEN")
	pontosVida = (d1 + d2 +1) * rodadas
	print (pontosVida)

elif:
	print ("FRAQUEZA")
	pontosVida = d1 * d2
	print (pontosVida)
		
	