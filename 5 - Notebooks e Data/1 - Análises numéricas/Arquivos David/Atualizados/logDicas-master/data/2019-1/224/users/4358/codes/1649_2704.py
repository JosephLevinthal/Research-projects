preco=float(input("Digite o preco:"))
pag=float(input("Digite o pagamento:"))
if(preco>pag):
	falta=preco-pag
	print(round(falta))
else:
	troco=preco-pag
	print(round(troco,2))