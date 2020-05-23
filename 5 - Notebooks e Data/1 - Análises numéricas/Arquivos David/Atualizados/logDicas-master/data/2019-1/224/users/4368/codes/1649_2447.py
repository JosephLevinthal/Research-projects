preco = float(input("Digite o preco:"))
pag = float(input("Digite o pagamento:"))
if preco>pag:
	print("Falta" , preco - pag)
else:	
	print("Troco de" , pag - preco)
