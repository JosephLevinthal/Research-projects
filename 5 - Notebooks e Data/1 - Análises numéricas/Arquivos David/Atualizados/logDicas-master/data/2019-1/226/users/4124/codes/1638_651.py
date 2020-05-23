h = float(input("Digite a altura: "))
sex = input("Digite o sexo (M/F): ").upper()

if(sex == "M"):
	imc = (72.7 * h) - 58
else:
	imc = (62.1 * h) - 44.7
print(round(imc,2))