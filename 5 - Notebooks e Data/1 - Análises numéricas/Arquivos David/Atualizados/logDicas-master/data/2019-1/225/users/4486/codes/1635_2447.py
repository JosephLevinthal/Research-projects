preco = float(input())
pagamento = float(input())

if (preco>pagamento):
	x = preco - pagamento
	x = round(x,2)
	msg = "falta " + str(x)
else:
	y = pagamento - preco
	y = round(y,2)
	msg = "troco de " + str(y)
print(msg)