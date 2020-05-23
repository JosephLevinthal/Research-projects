preco = float(input("preco: "))
pagamento = float(input("pagamento: "))

if (preco > pagamento):
	x = preco - pagamento
	print("Falta",round(x,2))

else:
	y = pagamento - preco
	print("Troco de",round(y,2))