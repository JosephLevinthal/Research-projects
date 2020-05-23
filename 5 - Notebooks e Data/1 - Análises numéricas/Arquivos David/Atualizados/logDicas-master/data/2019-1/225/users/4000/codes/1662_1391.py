c = float(input("Qual o consumo de energia ? "))
if(c<=150):
	emp = (0.60 * c) + 5
else:
	emp = (0.75 * c) + 16
print(round(emp, 2))

	