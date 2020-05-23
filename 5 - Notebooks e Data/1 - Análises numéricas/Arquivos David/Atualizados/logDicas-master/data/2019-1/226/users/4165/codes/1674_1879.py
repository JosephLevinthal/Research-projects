h = float(input("informe o numero de horas extras: "))
f = float(input("informe o numero de horas nao cumpridas"))
print(h," extras e ", f, " de falta")
H = h - (1/4 * f)
if(H <= 400):
	g = 100.0
elif(H > 400 ):
	g = 500.0
print("R$",round(g, 2))
