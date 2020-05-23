p = float(input("Valor do percurso: "))
tc = input("Tipo de carro: (A) ou (B).")
if(tc.upper() == "A"):
	c = p/8
if(tc.upper() == "B"):
	c = p/12
	
print(round(c,2))
	