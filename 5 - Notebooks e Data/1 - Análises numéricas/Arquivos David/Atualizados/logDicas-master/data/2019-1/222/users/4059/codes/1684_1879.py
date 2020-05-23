# Ao testar sua solução, não se limite ao caso de exemplo.

he = float(input("Numero de horas extras: "))
hf = float(input("Numero de horas nao trabalhadas: "))

h = he - hf/4

print("{} extras e {} de falta".format(he,hf))

if (h > 400):
	print("R$ 500.0")
else:
	print("R$ 100.0")