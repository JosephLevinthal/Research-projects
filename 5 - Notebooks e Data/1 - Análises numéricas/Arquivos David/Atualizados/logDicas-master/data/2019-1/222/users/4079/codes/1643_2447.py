preco=float(input("preco:"))
pagamento=float(input("pagamento:"))
if(preco > pagamento):
	print("Falta",round(preco-pagamento,1))
else:
	print("Troco de ", round(pagamento - preco,1))
