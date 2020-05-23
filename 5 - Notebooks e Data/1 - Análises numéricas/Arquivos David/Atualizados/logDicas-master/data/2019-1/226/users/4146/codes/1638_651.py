h = float(input("Altura: "))
s = input("Sexo: ")

pm = round((72.7 * h) - 58, 2)
pf = round((62.1 * h) - 44.7, 2)

if(s.upper() == "M"):
	print(pm)
else:
	print(pf)