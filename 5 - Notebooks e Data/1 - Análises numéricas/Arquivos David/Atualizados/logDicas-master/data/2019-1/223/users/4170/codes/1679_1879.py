# Ao testar sua solução, não se limite ao caso de exemplo.
he = float(input("Numero de horas extras: "))
hf = float(input("Numero de horas que faltou: "))
H = he - 1/4 * (hf)
print(he, "extras e", hf, "de falta")
if(H>400):
	print("R$", 500.0)
else:
	print("R$", 100.0)