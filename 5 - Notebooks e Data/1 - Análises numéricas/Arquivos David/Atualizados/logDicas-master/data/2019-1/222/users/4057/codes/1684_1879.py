# Ao testar sua solução, não se limite ao caso de exemplo.]
E = float(input("numero de horas extras: "))
F = float(input("numero de horas que o funcionario faltou: "))

H = (E) - 1/4 *  (F)

if (H > 400):
	G = 500.0
	print(E, "extras e ", F, " de falta")
	print("R$ ",round(G, 2))
elif (H > 0) and (H <= 400):
	G = 100.0
	print(E, "extras e ", F, " de falta")
	print("R$ ",round(G, 2))