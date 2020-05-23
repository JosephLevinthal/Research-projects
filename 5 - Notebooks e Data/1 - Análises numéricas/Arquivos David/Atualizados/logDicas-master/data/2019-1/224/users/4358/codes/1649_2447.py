preco=float(input("Digite o preco:"))
pag=float(input("Digite o pagamento:"))
if(preco>pag):
	x=preco-pag
	print("Falta",x)
else:
	y=pag-preco
	print("Troco de",y)
	