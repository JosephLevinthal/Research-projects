preco= float(input("Preco: "))
pag= float(input("Pagamento: "))

if (preco > pag):
	print("Falta",  preco - pag)
	
else:
	print("Troco de", pag - preco)