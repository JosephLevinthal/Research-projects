e=float(input("numero de horas extras: "))
f=float(input("numero de horas que o funcionario faltou: "))
print(e,"extras e", f, "de falta")
h=e-(1/4*f)
if(h>400):
	x=500.00
elif(h<=400):
	x=100.00
print("R$", x)




