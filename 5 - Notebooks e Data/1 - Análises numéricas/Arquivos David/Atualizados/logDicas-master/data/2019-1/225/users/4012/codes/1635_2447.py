preco = float(input("digite preco: "))
pagamento = float(input("digite pagamento: "))
X = preco - pagamento
Y = pagamento - preco

if preco > pagamento:
	print("Falta", X)
else:
	print("Troco de", Y)