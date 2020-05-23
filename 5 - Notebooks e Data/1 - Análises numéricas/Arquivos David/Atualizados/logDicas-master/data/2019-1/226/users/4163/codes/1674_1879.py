# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("numero de horas extras: "))
f = float(input("numero de faltas em horas: "))


print(e,"extras e",f,"de falta")

h = e -(1/4 * f)

if(h <= 400):
	g = 100.0
	print("R$",round(g,2))
elif(h > 400):
	g = 500.0
	print("R$",round(g,2))
	