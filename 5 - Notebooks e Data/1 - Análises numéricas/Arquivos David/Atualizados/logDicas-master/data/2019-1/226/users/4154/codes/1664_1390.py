c = float(input('consumo: '))

if c <= 100:
	print(round(c*1.2,2))
else:
	print(round(c*1.4+25,2))