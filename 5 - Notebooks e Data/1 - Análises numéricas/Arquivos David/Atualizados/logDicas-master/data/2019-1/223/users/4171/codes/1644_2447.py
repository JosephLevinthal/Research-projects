preco = float(input("preco: "))
pag = float(input("pagamento: "))

if preco > pag:
	x = preco - pag
	print("Falta",x)
else:
	pag < preco
	y = pag - preco
	print("Troco de",y)