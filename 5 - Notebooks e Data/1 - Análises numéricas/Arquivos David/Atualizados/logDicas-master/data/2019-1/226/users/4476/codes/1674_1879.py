# Ao testar sua solução, não se limite ao caso de exemplo.
nhe = float(input("numero de horas extras: "))
nhnt = float(input("numero de horas faltadas: "))

h = (nhe) - (1/4*nhnt)

if (h>400):
	g = round(500.00, 2)
else:
	g = round(100.00, 2)
print(nhe, "extras e", nhnt, "de falta")
print("R$", g)