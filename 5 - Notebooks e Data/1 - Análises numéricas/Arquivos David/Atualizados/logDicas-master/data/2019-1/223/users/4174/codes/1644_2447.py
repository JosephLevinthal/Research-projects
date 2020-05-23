preco = float(input("preco: "))
pagamento = float(input("pagamento: "))
if (preco > pagamento):
	print("Falta", preco - pagamento)
else:
	print("Troco de", pagamento - preco)