a = float(input("Insira a altura: "))
s = input("Insira o sexo (M / F): ")

m = (72.7 * a) - 58
f = (62.1 * a) - 44.7

if(s.upper() == "F"):
	print(round(f, 2))
else:
	print(round(m, 2))