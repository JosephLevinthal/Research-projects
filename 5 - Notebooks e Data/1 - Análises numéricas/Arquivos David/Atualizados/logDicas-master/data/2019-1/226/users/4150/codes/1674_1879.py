# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input("numero de horas extras: "))
b = float(input("numero de horas que faltou: "))

print(a, "extras e", b, "de falta")

h = (a - (0.25*b))

if (h > 400):
	print("R$ 500.0")
else:
	if(h<=400):
		print("R$ 100.0")