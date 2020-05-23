
q = int(input("quantidade de jogos: "))
p1 = float(input("preco do jogo:" ))


 

if (q == 2):
	p2 = float(input("preco 2: "))
	desconto = p2 * 0.25
	preco = p1 +( p2 - desconto)

else: 	
	preco = p1 

print(round(preco, 2))

	