a = float(input("altura: "))
s = input("sexo: (M/F) ")


if(s.upper() == "M"):
	h = (72.7*a) - 58
	print(round(h, 2))
else:
	m = (62.1*a) - 44.7
	print(round(m, 2))