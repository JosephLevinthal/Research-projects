preco=float(input("digite o valor: "))


if(preco>=200):
	
	pago= preco-((5*preco)/100)
	
	print(round(pago,2))
	
else:
	print(preco)