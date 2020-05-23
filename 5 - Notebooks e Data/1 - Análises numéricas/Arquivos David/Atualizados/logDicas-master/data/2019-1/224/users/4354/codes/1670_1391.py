consumo = float(input("digite o consumo de energia: "))
if(consumo <= 150):
	tarifa = 0.6 * consumo + 5
	print(round(tarifa,2))
else:
	tarifa = 0.75 * consumo + 16
	print(round(tarifa,2))