# Ao testar sua solução, não se limite ao caso de exemplo.
he = float(input("numero de horas extras: "))
nhf = float(input("numero de horas em que faltou: "))
h = (he) - 1/4 * (nhf)
print(he,"extras e" , nhf,"de falta")
if (h <= 400):
	G = "R$ 100.0"
	print(G)
else: 
	G = "R$ 500.0"
	print(G)
	
