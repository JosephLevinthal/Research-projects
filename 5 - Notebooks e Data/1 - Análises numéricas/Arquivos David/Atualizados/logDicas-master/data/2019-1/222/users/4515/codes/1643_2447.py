
preco=float(input("Informe preco :"))
pagamento=float(input("Informe pagamento :"))
if(preco > pagamento):
	falta=round(preco-pagamento,2)
	print("Falta ",falta)
else:	
	troco=round(pagamento-preco,2)
	print("Troco de ",troco)