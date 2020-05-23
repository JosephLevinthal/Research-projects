perc = float(input("percurso: "))
tipo = input("tipo de carro, A ou B: ")
x1 = 1/8
x2 = 1/12
if tipo == "A":
	print(round(perc*x1, 2))
else:
	print(round(perc*x2, 2))
