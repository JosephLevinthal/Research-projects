h= float(input("horas ministradas:"))
if h<=20:
	print(round(50 * h), 2)
else:
	print(round(50 + 70 *( h - 20), 2))