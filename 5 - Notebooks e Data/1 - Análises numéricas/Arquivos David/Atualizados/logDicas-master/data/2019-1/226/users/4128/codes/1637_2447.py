preco = float(input("ta caro o alguel: "))
pag = float(input("pague o aluguel: "))

if( preco > pag):
	x = preco - pag
	print("Falta", x )
else: 
	y = pag - preco
	print("Troco de", y)