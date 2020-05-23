c = float(input("Cosumo de agua: "))
if (c < 10):
	cont = (c * 3) + 30
	print(round(cont,2))
else:
	cont = (c * 3.50) + 30
	print(cont)