h = float(input("digite a altura: "))
s = input("digite o sexo: (M/F)  ")


if s.upper() == "M":
	a = (72.7*h)-58
	print(round(a,2))
if s.upper() == "F":
	b = (62.1*h)-44.7
	print(round(b,2))