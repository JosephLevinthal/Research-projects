hext= float(input("Horas extras trabalhadas: "))
faltas = float(input("Horas que faltou: "))

h = (hext) - (1/4)*faltas

if (h <= 400):
	print(hext, "extras e", faltas, "de falta")
	print("R$ 100.0")
else:
	print(hext, "extras e", faltas, "de falta")
	print("R$ 500.0")
