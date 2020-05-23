ATAQUE = input("escolha o ataque")
D1 = int(input("qual o resultado do primeiro dado jogado"))
D2 = int (input("resultado do segundo dado"))
if (ATAQUE == "FURIA"):
	if (1 < D1 <= 8) and (1 <D2 <= 8):
		DANO = 10 + D1 + D2
		print(DANO)
	else:
		print("Entrada invalida")
elif (ATAQUE == "GRITO"):
	if (1 < D1 <= 8) and (1 < D2 <= 8):
		DANO = 6 + D1 + D2
		print(DANO)
	else:
		print("Entrada invalida")
elif ( ATAQUE == "TOQUE"):
	if (1 < D1 < 8 ) and ( 1 < D2 < 8):
		DANO = (D1 + D2)**2
		print(DANO)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
	