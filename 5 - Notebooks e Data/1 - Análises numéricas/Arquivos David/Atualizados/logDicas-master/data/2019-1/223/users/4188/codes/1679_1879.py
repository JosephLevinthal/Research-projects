# Ao testar sua solução, não se limite ao caso de exemplo.
he=float(input("horas extras: "))
f=float(input("faltas: "))
print(he,"extras e",f,"de falta")
H=he-(1/4)*f
if(H>=400):
	p=500.00
	print("R$",round(p,2))
if(H<=400):
	p=100.00
	print("R$",round(p,2))