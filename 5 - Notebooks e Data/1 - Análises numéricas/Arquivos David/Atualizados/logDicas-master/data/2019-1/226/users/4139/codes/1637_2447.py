preco = float(input("valor de preco:"))
pago = float(input("valor a ser pago:"))

if (preco > pago):
	x = preco - pago
	print("Falta ",round(x,2))
	
else:
	y = pago - preco
	print("Troco de ",round(y,2))