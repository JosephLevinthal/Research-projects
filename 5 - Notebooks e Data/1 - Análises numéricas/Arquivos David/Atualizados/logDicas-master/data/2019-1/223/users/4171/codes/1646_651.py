h = float(input("Altura: "))
s = input("Sexo: (M/F)")

if s == "M":
	P = (72.7 * h) - 58
	print(round(P,2))
else:
	P = (62.1 * h) - 44.7
	print(round(P,2))