# Ao testar sua solução, não se limite ao caso de exemplo.
a= float(input("horas extras: "))
b= float(input("numero de horas: "))

print(a, "extras e ", b, "de falta")

h = a - (1/4*b)

if(h<=400):
	g=100.0
	print("R$", round(g, 2))
elif(h>400):
	g=500.0
	print("R$", round(g, 2))