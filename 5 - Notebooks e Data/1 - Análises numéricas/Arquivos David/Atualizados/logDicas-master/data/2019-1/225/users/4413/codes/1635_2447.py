preco = float(input("numero: "))
pagamento = float(input("numero: "))
if(preco>pagamento):
	x = round(preco - pagamento, 2)
	print("Falta", x)
else:
	y = round(pagamento - preco, 2)
	print("Troco de", y)

	