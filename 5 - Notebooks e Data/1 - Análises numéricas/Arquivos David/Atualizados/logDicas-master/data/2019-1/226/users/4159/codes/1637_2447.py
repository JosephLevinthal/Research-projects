preco = float(input("valor da compra: "))
pagar = float(input("valor pago: "))
if(preco > pagar):
	x = str(round(preco-pagar, 2))
	print("Falta "+ x)
else:
	x = str(round(pagar-preco, 2))
	print("Troco de "+ x)