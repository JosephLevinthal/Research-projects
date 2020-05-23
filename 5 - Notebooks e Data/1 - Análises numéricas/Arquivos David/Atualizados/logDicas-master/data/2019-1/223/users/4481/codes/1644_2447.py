preco = float(input(" qual o valor? "))
pagamento = float(input(" qual o pagamento? "))
if(preco>pagamento):
	mensagem = "Falta " + str(preco-pagamento)
else:
	mensagem = "Troco de " + str(pagamento-preco)
print( mensagem)
