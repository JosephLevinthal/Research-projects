preco=float(input("preco:"))
pagamento=float(input("pagamento:"))
if(preco>pagamento):
	d=(round(preco-pagamento, 2))
	print("Falta", d)
else:
	d=(round(pagamento-preco, 2))
	print("Troco de", d)