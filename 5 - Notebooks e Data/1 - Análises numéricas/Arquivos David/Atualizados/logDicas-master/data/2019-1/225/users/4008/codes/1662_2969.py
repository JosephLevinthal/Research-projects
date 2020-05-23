j = int(input("quantidade de jogos(1 / 2): "))
j1 = float(input("preco do primeiro jogo: "))
j2 = float(input("preco do segundo "))
d = j1 + (j2 - j2*25/100)
if(j == 2):
	print(round(d, 2))
else:
	print(round(j1, 2))
	