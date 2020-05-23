gold = int(input("Determinar a quantidade de ouro: "))
armor = input("Determinar material da armadura: ").upper()
d = int(input("Determinar fator de destreza: "))

I = 30*d-20
M = 15*d-1
P = 20*d-18

if (d >= 1 and d <=8):
	if (armor == "INTEIRA") and (gold >= 200):
		print(I)
	elif (armor == "MALHA") and (gold >= 50):
		print(M)
	elif (armor == "PLACA") and (gold >= 100):
		print(P)
	else:
		print("PO insuficiente")