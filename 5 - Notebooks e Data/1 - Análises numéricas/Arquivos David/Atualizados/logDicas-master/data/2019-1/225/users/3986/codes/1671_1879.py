# Ao testar sua solução, não se limite ao caso de exemplo.
E=float(input("numero de horas extras :"))
F=float(input("numero de horas faltadas :"))
H=E - 1 / 4 * F
if (H > 400) :
	print(E, "extras","e",F,"de falta")
	print("R$ 500.0")
else :
	print(E,"extras e",F,"de falta")
	print("R$ 100.0")