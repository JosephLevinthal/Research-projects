e = float(input("digite as horas extras: "))
f = float(input("digite as faltas: "))
h = e - (1/4 * f)
q = 500.0
c = 100.0
if h > 400:
	print(e,"extras e",f,"de falta")
	print("R$",q)
else:
	print(e,"extras e",f,"de falta")
	print("R$",c)