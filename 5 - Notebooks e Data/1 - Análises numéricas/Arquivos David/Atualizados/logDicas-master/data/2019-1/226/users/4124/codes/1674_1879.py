# Ao testar sua solução, não se limite ao caso de exemplo.
h = float(input("Horas extras: "))
f = float(input("Horas faltadas: "))
h2 = h - (1/4) * f
print(h ,"extras e", f, "de falta")
if(h2 > 400):
	g = 500.0
else:
	g = 100.0
print("R$ ",g)