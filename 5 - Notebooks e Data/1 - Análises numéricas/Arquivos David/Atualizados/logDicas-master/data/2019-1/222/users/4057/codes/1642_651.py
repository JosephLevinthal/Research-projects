a = float(input("Qual a sua altura? "))
s = input("Sexo (M ou F): ")

if (s.upper() == "M"):
	homens = (72.7 * a) - 58
	print(round(homens, 2))
else: 
	mulheres = (62.1 * a) - 44.7
	print(round(mulheres, 2))