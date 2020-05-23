# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("numero de horas extra: "))
b=float(input("numero de horas de falta: "))
print(a,"extras e",b,"de falta")
H=a-1/4*b
if(H>=400):
	r=500.00
	print("R$",round(r, 2))
elif(H<=400):
	r=100.00
	print("R$",round(r, 2))
	