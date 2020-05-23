jogos = int(input("quantidade de jogos: "))
preco1 = float(input("preco jogo 1: "))

if(jogos == 2):
	preco2 = float(input("preco do jogo 2: "))
	desconto = preco2-preco2*0.25
	valor = desconto+preco1
	x= round(valor, 2)
	print(x)
else:
	valor = preco1
	y = round(valor, 2)
	print(y)