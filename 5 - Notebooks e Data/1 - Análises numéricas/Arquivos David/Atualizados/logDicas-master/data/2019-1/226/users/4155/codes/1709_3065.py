x = input("tipo de ataque: ").upper()
n = int(input("valor sorteado: "))
z = int(input("numero de turnos: "))

if(n < 1 or n > 4):
	print("Entrada invalida")
	
else:
	if(x == "CUSPE"):
		p = n * 2 * z
		print(p)
	elif(x == "PATADA"):
		print((2 * n) - 5)
	elif(x == "CAUDA"):
		print(n * z)