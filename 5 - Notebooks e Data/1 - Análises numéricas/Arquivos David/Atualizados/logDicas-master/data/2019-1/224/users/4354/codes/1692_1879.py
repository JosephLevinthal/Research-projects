# Ao testar sua solução, não se limite ao caso de exemplo.
h_extra = float(input("Numero de horas extras: "))
h_faltas = float(input("Numero de horas de falta: "))
H = h_extra - (1/4 * h_faltas)
if(H > 400):
	print(h_extra,"extras e",h_faltas,"de falta")
	print("R$ 500.0")
if(H < 400):
	print(h_extra,"extras e",h_faltas,"de falta")
	print("R$ 100.0")
