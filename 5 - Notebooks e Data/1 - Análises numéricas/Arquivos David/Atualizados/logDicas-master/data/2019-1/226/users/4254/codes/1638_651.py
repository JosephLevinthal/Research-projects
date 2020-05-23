alt = float(input("Valor da altura: "))
sex = input("Sexo masc.(M) ou fem.(F): ")
if(sex.upper() == "M"):
	p = (72.7*alt) - 58
if(sex.upper() == "F"):
	p = (62.1*alt) - 44.7
	
print(round(p,2))
	