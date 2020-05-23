consumo = float(input("comido:"))
total1 = consumo + 10/100 * consumo
total2 = consumo + 6/100 * consumo

if(consumo <= 300):
	print(round(total1,2))
else:
	print(round(total2,2))