alt = float(input("altura: "))
sex = input("sexo: ")
pesoh = (72.7 * alt) - 58
pesom = (62.1 * alt) - 44.7
if (sex.upper() == "M"):
	print(round(pesoh,2))
if (sex.upper() == "F"):
	print(round(pesom,2))