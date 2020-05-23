E=float(input("numero de horas extras: "))
F=float(input("numero de horas que o funcionario faltou: "))
H=round((E-1/4*F), 2)
if(H>400):
	print(E,"extras e",F, "de falta")
	print("R$ 500.0")
elif(H<=400):
	print(E,"extras e",F,"de falta")
	print("R$ 100.0")