preco = float(input("preco: "))
pagamento = float(input("pagamento: "))


if(preco>pagamento):
	X = preco - pagamento
	X = round(X, 2)
	print("Falta", X)
else:
	Y = pagamento - preco
	Y = round(Y, 2)
	print("Troco de", Y)