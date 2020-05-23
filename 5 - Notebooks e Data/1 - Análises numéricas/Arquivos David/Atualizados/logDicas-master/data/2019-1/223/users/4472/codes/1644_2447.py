preco = float(input("Valor do Produto: "))
pagamento = float(input("Valor do Pagamento: "))

if preco > pagamento:
	x = preco - pagamento
	print ("Falta ",round(x,2))
else:
	y = pagamento - preco
	print("Troco de ",round(y,2))
	