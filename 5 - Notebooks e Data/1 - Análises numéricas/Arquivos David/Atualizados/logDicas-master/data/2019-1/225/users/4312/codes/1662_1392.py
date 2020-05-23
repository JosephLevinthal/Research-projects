consumo = float(input("consumo do cliente foi? "))
pag = 30

if (consumo < 10):
	total = pag + 3*consumo
else:
	total = pag + 3.50*consumo
print(round(total, 2))