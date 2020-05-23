preco = float(input(" Digite o preco "))
pagamento = float(input(" Digite o pagamento "))

if (preco > pagamento):
	b = round(preco-pagamento,2)
	print(" Falta ", b)
else:
	g = round(pagamento-preco,2)
	print(" Troco de", g)

	
