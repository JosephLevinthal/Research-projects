compra = float(input("Valor da compra sem desconto:"))

if(compra>=200):
	total = compra - (0.05*compra)
	print(round(total, 2))
else:
	print(round(compra, 2))