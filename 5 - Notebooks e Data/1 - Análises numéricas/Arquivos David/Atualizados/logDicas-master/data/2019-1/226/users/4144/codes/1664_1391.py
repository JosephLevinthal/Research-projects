a = int(input("digite o consumo de energia: "))
if (a <= 150):
	cons = (0.6 * a) + 5
else:
	cons = (0.75 * a) + 16
print(round(cons,2))
