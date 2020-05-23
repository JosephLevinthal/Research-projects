# Ao testar sua solução, não se limite ao caso de exemplo.
E=float(input("NUMERO DE HORAS EXTRAS:"))
F=float(input("NUMERO DE HORAS NAO TRABALHADAS:"))
H=E-1/4*F

if(H>=0):
	if(H<=400):
		
		print(E, "extras e", F, "de falta")
		print("R$", round(100.00,2))
	else:
		
		print(E, "extras e", F, "de falta")
		print("R$", round(500.00,2))
else:
	print("entrada invalida")