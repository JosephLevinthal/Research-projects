preco = float(input("Preco do produto: "))
pagamento = float(input("Pagamento: "))

if preco > pagamento:
	falta = preco - pagamento
	print("Falta " + str(round(falta, 2)))
elif preco <= pagamento:
	troco = pagamento - preco
	print("Troco de " + str(round(troco, 2)))
