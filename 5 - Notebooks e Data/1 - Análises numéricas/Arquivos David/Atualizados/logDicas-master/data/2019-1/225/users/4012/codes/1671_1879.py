E = float(input("digite hora extra: "))
F = float(input("digite faltas: "))
print(E, "extras e", F, "de falta")

H = E - (1 / 4) * F

if (H > 400):
	G = 500.00
	print("R$ ", round(G, 2))
elif (H <= 400):
	G = 100.00
	print("R$ ", round(G, 2))


