# Ao testar sua solução, não se limite ao caso de exemplo.

he = abs(float(input("numero de horas extras: ")))
hf = abs(float(input("numero de horas faltadas: ")))

H = he - (0.25 * hf)

print(he,"extras e", hf,"de falta")
if H > 400:
	G = float(500)
	print("R$", G)
elif H <= 400:
	G = float(100)
	print("R$", G)
