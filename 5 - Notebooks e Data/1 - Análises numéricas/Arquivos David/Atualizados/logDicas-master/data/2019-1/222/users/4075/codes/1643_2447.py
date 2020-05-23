preco= float(input("leia o preco:" ))
pagamento= float(input("leia o pagamento:" ))
if (preco>pagamento):
	x= preco-pagamento
	x1=round(x,2)
	print("Falta", x1)
else:
	y= pagamento-preco
	y1=round(y,2)
	print("Troco de", y1)
	


