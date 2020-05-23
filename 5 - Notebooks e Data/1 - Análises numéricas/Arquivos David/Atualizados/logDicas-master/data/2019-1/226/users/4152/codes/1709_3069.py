x = input("Digite aqui o nome do ataque realizado pela Banshee: ").upper()
d1 = int(input("Digite aqui os valores sorteados em cada um dos dois dados: "))
d2 = int (input("Digite aqui os valores sorteados em cada um dos dois dados: "))
calf = 10 + (d1 + d2)
calg = 6 + (d1 + d2)
calt = (d1 + d2) ** 2
if (x != "FURIA") and (x != "GRITO") and (x != "TOQUE") or (d1 < 1) and (d2 > 8) or (d2 < 1) and (d1 > 8):
	total = "Entrada invalida"
else:
	if (x == "FURIA"):
		total = calf
	elif (x == "GRITO"):
		total = calg
	else:
		total = calt
print(total)

	