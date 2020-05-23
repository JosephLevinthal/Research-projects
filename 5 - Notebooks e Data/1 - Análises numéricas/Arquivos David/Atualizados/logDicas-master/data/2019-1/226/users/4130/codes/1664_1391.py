k = float(input("Quantidade kWh consumidos: "))

x1 = (0.60 * k) + 5.00
x2 = (0.75 * k) + 16.00

if(k <= 150):
	print(x1)
if(k > 150):
	print(x2)