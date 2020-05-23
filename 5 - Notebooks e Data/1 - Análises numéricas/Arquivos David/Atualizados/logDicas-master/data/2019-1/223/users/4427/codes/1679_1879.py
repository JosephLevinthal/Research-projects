# Ao testar sua solução, não se limite ao caso de exemplo.
extras = float(input())
faltas = float(input())
H = float()
meio = float()

meio = 1/4*faltas

H = extras - meio

if H > 400:
	print(extras, "extras e ", faltas,"de falta")
	print("R$ 500.0")
elif H <= 400:
	print(extras, " extras e", faltas, "de falta")
	print("R$ 100.0")