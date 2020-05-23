preco = float(input("qual o preco : "))
pagamento = float(input("valor do pagamento: ")) 

falta = preco - pagamento
troco = pagamento - preco 

if (preco > pagamento):
	x = (round(falta, 2))
	mensagem = "Falta"
	print(mensagem, x)
	
else :
	y = (round(troco, 2))
	mensagem = "Troco de"
	print(mensagem, y)

		
