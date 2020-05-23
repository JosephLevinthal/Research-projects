preco = float(input("Preco: "))
pagamento = float(input("Pagamento: "))

if(preco > pagamento):
	print("Falta " + str(round(preco - pagamento, 2)))
else:
	print("Troco de " + str(round(pagamento - preco, 2)))