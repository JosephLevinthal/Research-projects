d = float(input("percurso: "))
tipo = input("tipo de carro: (A/B)")

if tipo == "B":
	c = 12.5/d*100
	print(round(c,2))
if tipo == "A":
	c = 8/d*100
	print(round(c,2))