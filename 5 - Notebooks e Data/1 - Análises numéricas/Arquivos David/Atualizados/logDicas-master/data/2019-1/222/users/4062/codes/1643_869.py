compra = float(input("valor da compra: "))
if	(compra >= 200.0):
	print(round(compra - (compra * 0.05), 2 ))
else:
	print(round(compra ))