t = float(input("Horas: "))
n = float(input("Horas: "))

print(t, "extras e", n, "de falta")

h = t - (1/4*n)

if (h <= 400):
	g = 100.0
	print("R$", round(g, 2))
else:
	g = 500.0
	print("R$", round(g, 2))
