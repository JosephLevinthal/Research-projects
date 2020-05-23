#Furia = 10 + (2 a 16)
#Grito = 6 + (2 a 16)
#Toque = (Dado 1 + dado 2)*2

ataque = input("Tipo de ataque: FURIA/GRITO/TOQUE?")
dado1 = int(input("Valor do primeiro dado:"))
dado2 = int(input("Valor do segundo dado: "))
dados = (dado1+dado2)

if ((2 <= dado1 <= 8 and 2<=dado2<=8) and ataque.upper() == "FURIA" or ataque.upper() == "GRITO" or ataque.upper() == "TOQUE"):
	if (ataque.upper() == "FURIA"):
		a = 10 + (dados)
		print(a)
	elif (ataque.upper() == "GRITO"):
		y = 6 + (dados)
		print(y)
	else:
		x = (dados)**2
		print(x)
else:
	print("Entrada invalida")
