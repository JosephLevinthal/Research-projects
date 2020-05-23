# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("extras: "))
F = float(input("faltas: "))

H = E - ((1/4) * F)

if H > 400.0:
	G = 500.0
else:
	G = 100.0
	
print(E,"extras e",F ,"de falta")
print("R$",round(G, 2))