preco = float(input("Valor do preco: "))
pag = float(input("Valor do pagamento: "))

if(preco > pag):
	dif = preco - pag
	print("Falta", round(dif,2))
else:
	dif = pag - preco
	print("Troco de", round(dif,2))
