preco = float(input("digite preco: "))
pag = float(input("digite o pagamento: "))
x = preco - pag
y = pag - preco
if (preco > pag):
	print("Falta",round(x,2))
else:
	print("Troco de",round(y,2))