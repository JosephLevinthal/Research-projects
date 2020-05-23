consumo=int(input("consumo de energia: "))
lim=150
if (consumo<=lim):
	print(float(round(0.6*consumo+5,2)))
else:
	print(float(round(0.75*consumo+16,2)))
