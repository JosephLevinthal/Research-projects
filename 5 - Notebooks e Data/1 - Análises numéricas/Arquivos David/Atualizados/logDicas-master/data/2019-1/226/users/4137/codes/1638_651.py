alt = float(input("Qual sua altura:"))
sex = input("Qual seu sexo:")

if( sex.upper() == "M"):
	imc = (72.7 * alt) - 58
else:
	imc = (62.1 * alt) - 44.7

print(round(imc, 2))	