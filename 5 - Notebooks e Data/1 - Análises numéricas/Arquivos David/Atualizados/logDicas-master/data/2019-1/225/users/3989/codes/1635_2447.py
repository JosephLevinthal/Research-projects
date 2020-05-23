preco = float(input(""))
pagamento = float(input("")) 
if (preco>pagamento):
	x = (preco - pagamento)
	print("Falta", x)
else:
	y = (pagamento - preco)
	print("Troco de", y)

	
