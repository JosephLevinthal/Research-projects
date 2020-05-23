alt = float(input("Qual sua altura? "))
sexo = input("M/F: ")
m = round((72.7 * alt) - 58.0 , 2)
f = round((62.1 * alt) - 44.7 , 2)

if(sexo.upper() == "M"):
	print(m)
else:
	print(f)