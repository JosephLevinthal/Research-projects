preco=float(input())
valor=float(input())

if (preco > valor):
	print("Falta",preco-valor)
else:
	print("Troco de",valor-preco)