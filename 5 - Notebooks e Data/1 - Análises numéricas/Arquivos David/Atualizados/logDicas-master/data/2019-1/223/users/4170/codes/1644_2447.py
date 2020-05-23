preco = float(input("aa:"))
pagamento = float(input("aa:"))

if (preco > pagamento):
	X = preco - pagamento
	print("Falta ", round(X,2))
else:
	Y = pagamento - preco
	print("Troco de ", round(Y,2))