compra = float(input("Preco da compra: "))
desc = (compra/100*5)

if(compra >= 200):
	print(round(compra - desc ,2))
else:
	print(round(compra, 2))