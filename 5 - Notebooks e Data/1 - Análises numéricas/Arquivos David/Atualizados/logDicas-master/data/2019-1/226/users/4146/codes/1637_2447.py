preco = float(input("Preco: "))
paga = float(input("Pagamento: "))

if (paga >= preco):
	Y = paga - preco
	print("Troco de ", round(Y, 2))
else:
	X = preco - paga
	print("Falta ", round(X, 2))
	


	