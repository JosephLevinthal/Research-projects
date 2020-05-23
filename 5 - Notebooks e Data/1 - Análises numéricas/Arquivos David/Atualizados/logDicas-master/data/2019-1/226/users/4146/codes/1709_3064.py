a = input("Ataque: ").upper()
b = int(input("Dado 1: "))
c = int(input("Dado 2: "))

if (1 <= b <= 10) and (1 <= c <= 10) and ((a == "AAMEUL") or (a == "HETHRADIAH") or (a == "RAKSHASA")):
	if (a == "AAMEUL"):
		dano = 8 + (c + b)
		print(dano)
	elif (a == "HETHRADIAH"):
		dano = 2 * (c + b)
		print(dano)
	elif (a == "RAKSHASA"):
		dano = 10 + (c + b)
		print(dano)
else:
	print("Entrada invalida")