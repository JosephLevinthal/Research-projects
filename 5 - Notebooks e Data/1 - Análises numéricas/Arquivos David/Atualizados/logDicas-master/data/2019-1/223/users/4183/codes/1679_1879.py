# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("Horas extras: "))
F = float(input("Horas de falta: "))

H = E - ((1/4) * F)
	
if (H > 400):
	print(E, "extras e", F, "de falta")
	print("R$", round(500.0,2))
else:
	print(E, "extras e", F, "de falta")
	print("R$", round(100.0,2))


	