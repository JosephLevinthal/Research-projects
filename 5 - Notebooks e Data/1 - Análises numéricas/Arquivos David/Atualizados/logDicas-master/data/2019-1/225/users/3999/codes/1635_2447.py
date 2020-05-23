preco=float(input("preco:"))
pagamento=float(input("pagamento:"))
x= preco-pagamento
y= pagamento-preco
if(preco>pagamento):
	print("Falta",round(x,2))
else:
	print("Troco de",round(y,2))
