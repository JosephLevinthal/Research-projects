preco=float(input("preco:"))
paga=float(input("pagamento: "))
sub=round(preco-paga, 2)
fal=round(paga-preco, 2)
if(preco>paga):
	print("Falta ", sub)
else:
	print("Troco de", fal)			