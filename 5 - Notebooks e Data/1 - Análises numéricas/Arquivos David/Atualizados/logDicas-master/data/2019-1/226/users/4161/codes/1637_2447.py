preco = float(input("preco: "))
pagamento = float(input("pagamento: "))
if (preco > pagamento):
	x = preco - pagamento
	print("Falta", x)
else:
	y = pagamento - preco
	print("Troco de ", y)