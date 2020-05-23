altura = float(input("Altura:"))
sexo = input("Sexo:")

if (sexo.upper()== 'M'):
	PI= (72.7*altura)-58
	print(round(PI, 2))
else:
	PI=(62.1*altura)-44.7
	print(round(PI, 2))