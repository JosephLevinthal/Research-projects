preco = float(input("Qual o preco da sua compra?"))
pagamento = float(input("Quanto voce pagou?"))

if(preco>pagamento):
	mensagem = "Falta " + str(preco-pagamento)
else:
	mensagem = "Troco de " + str(pagamento-preco)
print ( mensagem )