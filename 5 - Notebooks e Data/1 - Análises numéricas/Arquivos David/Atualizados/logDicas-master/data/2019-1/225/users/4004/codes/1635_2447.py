preco = float(input("preco: "))
pagamento = float(input("pagamento: "))

if preco > pagamento:
	x = preco - pagamento
	f = round(x, 2)
	print("Falta", f)
else:
	y = pagamento - preco
	f = round(y, 2)
	print("Troco de", f)