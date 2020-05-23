qj = int(input("Quantidade de jogos: "))
p1 = float(input("Preco do primeiro jogo: "))


if (qj == 1):
	print(round(p1,2))
else:
	p2 = float(input("Preco do segundo jogo: "))
	c = p1 + p2 - (p2*25/100)
	print(round(c,2))