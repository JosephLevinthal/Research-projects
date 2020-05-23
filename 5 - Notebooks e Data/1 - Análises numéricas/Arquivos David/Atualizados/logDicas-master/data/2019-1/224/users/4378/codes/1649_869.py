val=float(input("valor da compra: "))
if val>=200:
	print(round(val -0.05 * val, 2))
else:
	print(round(val, 2))
