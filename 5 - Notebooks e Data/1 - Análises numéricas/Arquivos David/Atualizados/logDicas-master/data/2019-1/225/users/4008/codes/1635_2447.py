preco = float(input("digite o preco: "))
pagamento = float(input("digite o pagamento: "))

x = preco - pagamento
y = pagamento - preco
if(preco > pagamento):
	mensagem = "Falta "
	print(mensagem, round(x, 2))
else:
	mensagem = " Troco de "
	print(mensagem, round(y, 2))