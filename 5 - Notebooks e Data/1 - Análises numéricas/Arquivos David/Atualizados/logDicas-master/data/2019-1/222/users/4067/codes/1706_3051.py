a = float(input("consumo: "))
if a >= 0:
	valor = a*0.60+5.00
	print(round(valor,2))
	if a >=150 or a == 250:
		valor = a*0.65+8.00
		print(round(valor,2))
	elif a > 250 or a ==350:
		valor = a*0.70+12.00
		print(round(valor,2))
	elif a > 350:
		valor = a*0.75+16.00
		print(round(valor,2))
else:
	print()
		