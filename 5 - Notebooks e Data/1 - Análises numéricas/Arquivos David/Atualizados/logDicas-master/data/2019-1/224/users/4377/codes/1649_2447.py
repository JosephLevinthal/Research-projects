preco=float(input("p"))
pagamento=float(input("pa"))
fa=preco-pagamento
troco=pagamento-preco

if(preco>pagamento):
	print("Falta", round(fa,2))
else:
	print("Troco de", round(troco,2))


	