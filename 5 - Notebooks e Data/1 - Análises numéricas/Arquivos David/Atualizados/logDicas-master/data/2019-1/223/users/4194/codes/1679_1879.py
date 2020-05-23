e = float(input("Horas extras: "))
f = float(input("Faltas: "))
print(e, "extras e", f, "de falta")

h = round(e - 1/4 * f, 2)

x = ("R$", h)
y = ("R$ 500.0")
z = ("R$ 100.0")

if(h > 400):
	print(y)
else:
	print(z)