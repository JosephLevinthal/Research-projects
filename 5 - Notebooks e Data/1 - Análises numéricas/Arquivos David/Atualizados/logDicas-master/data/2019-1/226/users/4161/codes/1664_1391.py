c = float(input("consume em kwh: "))
if (c > 0 and c < 150):
	total = (0.60*c) + 5.00
	print(round(total, 2))
else:
	total = 0.75*c + 16
	print(round(total, 2))