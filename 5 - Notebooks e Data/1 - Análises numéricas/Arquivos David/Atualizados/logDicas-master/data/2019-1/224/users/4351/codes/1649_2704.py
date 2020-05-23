nota=float(input("nota do marginal "))
boni=input("S ou N")

if (boni.upper()== "S"):
	nota=nota+((nota*10)/100)
else:
	nota=nota

print(round(nota, 2))
	