preco = float (input("Digite o valor do preco:"))
pagamento = float (input("Digite o valor do pagamento:"))
if (preco>pagamento):
	print( "Falta ", preco-pagamento)
else:
	print ("Troco de ", pagamento-preco)