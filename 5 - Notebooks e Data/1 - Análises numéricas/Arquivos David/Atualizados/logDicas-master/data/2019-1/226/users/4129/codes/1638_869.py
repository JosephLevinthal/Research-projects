compra = float(input("Valor da compra:"))
if(compra>=200):
	total = compra - (compra*0.05)
	print(round(total, 2))
else:
	print(round(compra, 2))