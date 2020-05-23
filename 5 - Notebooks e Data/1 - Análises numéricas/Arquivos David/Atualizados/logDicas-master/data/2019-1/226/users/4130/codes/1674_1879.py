e = float(input("Quantidade de horas extras: "))
f = float(input("Quantidade de faltas: "))

print(e," extras e ",f," de falta")

h = e - (1/4 * f)

if(h <= 400):
	g = 100.0
	print("R$", round(g, 2))
elif(h > 400):
	g = 500.0
	print("R$", round(g, 2))