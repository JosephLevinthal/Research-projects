preco = float(input("valor do preco: "))
pago = float(input("valor a pago: "))
troco = pago-preco 
falta = preco-pago
if(preco > pago):
	print("Falta ",round(falta,2))	
else:
	print("Troco de ",round(troco,2))