PO = int(input("pecas de ouro: "))
arma = input("arma: ").upper()
fator = int(input("sucesso: "))

if arma == "ESPADA" or arma == "MACHADO" or arma == "MARRETA" and (fator > 1 and fator <= 10):
	if arma == "ESPADA":
		preco = 100
		if PO >= preco:
			dano = fator*10
			print(dano)
		else:
			print("PO insuficiente")
	if arma == "MACHADO":
		preco = 30
		if PO >= preco:
			dano = fator + 3
			print(dano)
		else:
			print("PO insuficiente")
	if arma == "MARRETA":
		preco = 50
		if PO >= preco:
			dano = fator + 5
			print(dano)
		else:
			print("PO insuficiente")
else:
	print("Entrada invalida")
	