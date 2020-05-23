altura = float(input("Qual a altura?"))
sexo = input("M/F")
m = round((72.7 * altura) - 58.0 , 2)
f = round((62.1 * altura) - 44.7 , 2)

if(sexo.upper() == "M"):
	print(m)
else:
	print(f)