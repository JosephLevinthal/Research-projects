lanche= 5
salgado= 3,50
refrigerante= 4
mensagem=input("digite L ou S:")
mensagem=mensagem.upper()
quantidade=float(input("digite a quantidade de lanches ou salgados:"))
refrigerante=float(input("digite a quantidade de refrigerantes:"))
preco= quantidade+refrigerante
if(mensagem=="L"):
	lanche= 5*quantidade+refrigerante
	print(round(preco,2))
if(mensagem=="S"):
	salgado= 3,50*quantidade+refrigerante
			print(round(preco,2))

