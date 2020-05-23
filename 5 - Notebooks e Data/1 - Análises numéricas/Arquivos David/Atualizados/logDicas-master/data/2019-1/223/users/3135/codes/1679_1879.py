# Ao testar sua solução, não se limite ao caso de exemplo.
e= float(input("Insira o numero de horas extras:"))
f= float(input("Insira o numero de horas com ausencia:"))

print(e , "extras e",f, "de falta")

h= e - (1/4) * f
G1=100.00000
G2=500.00000

if(h>0):
	if(h<=400):
		print("R$",round(G1,2))
	else:
		print("R$",round(G2,2))