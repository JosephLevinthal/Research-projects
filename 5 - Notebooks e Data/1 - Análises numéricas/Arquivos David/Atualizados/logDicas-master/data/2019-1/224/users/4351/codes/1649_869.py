preco=float(input("valor da compra sem desconto "))

if (preco>=200):
	pagar=preco-((preco*5)/100)
else:
	pagar=preco
	
print(round(pagar, 2))
