X = float(input("digite o preco: "))
Y = float(input("digite o valor do pagamento: "))


if X > Y:
	print("Falta",(round (X-Y,1)))
else:
	print("Troco de",(round (Y-X,1)))