preco = float(input("Digite o preco: "))
pag = float(input("Informe o pagamento: "))
if(preco > pag):
	x = preco - pag
	round(x, 2)
	print("Falta",x,)
else: 
	y = pag - preco
	round(y, 2)
	print("Troco de",y,)

	