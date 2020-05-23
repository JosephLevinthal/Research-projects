preco = float(input())
pagamento = float(input())

if( preco > pagamento):
	print("Falta",preco-pagamento)
else:
	print("Troco de ",pagamento-preco)