Q = int(input("Quantidade de jogos (1 / 2): "))
j1 = float(input("Valor do jogo 1: "))

if(Q == 2):
	j2 = float(input("Valor do jogo 2: "))
	total = j1 + (j2 * 0.75)
else:
	total = j1
	
print(round(total, 2))