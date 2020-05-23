preco = float(input("Qual o preco? "))
pagamento = float(input("Quanto sera o pagamento? "))

if (preco>pagamento):
	mensagem = "Falta " + str(preco-pagamento)
	
else:
	mensagem = "Troco de " + str(pagamento-preco)
print(mensagem)