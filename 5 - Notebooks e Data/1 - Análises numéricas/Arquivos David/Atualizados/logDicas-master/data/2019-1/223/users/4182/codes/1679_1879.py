extras = float(input())
faltas = float(input())
print(extras,"extras","e",faltas,"de falta")

H = extras - 1/4*(faltas)

if (H > 400):
	g = 500.00
else:
	g = 100.00
print("R$",round(g,2))