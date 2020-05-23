preco=float(input("Digite o valor do preco: "))
pagamento=float(input("Digite o valor do pagamento: "))
if(preco>pagamento):
   preco=preco-pagamento
   preco=round(preco,2)
   print("Falta ",preco)
else:
	pagamento=pagamento-preco
	pagamento=round(pagamento,2)
	print("Troco de ",pagamento)