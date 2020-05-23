# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("horas extra:"))
F = float(input("horas de falta:"))
print (E , "extras e" , F , "de falta")
H = E - (1 / 4 * F)
if (H > 400):
	G = 500.0
	print("R$" , round(G , 2))
else:
	G = 100.0
	print("R$" , round(G , 2))