preco = float(input("Preco:"))
pagam = float(input("Pagamento:"))
if(preco>pagam):
	falta = preco-pagam
	print("Falta ", falta)

else:
	troco = pagam-preco
	print("Troco de ", troco)