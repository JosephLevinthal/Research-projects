ce= float(input("Valor do consumo de energia: "))
if (ce <= 150):
	tf = ((ce * 0.60) + 5.00)
else:
	tf = ((ce * 0.75) + 16.00)
print(round(tf, 2))