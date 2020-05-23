# Ao testar sua solução, não se limite ao caso de exemplo.
extras=float(input("numero de horas extras: "))
faltas=float(input("numero de horas faltadas: "))
h= extras - (1/4 * faltas)
print(extras, "extras e", faltas, "de falta")
if (h>400):
	print("R$ 500.0")
elif (h<=400):
	print("R$ 100.0")
	
	
