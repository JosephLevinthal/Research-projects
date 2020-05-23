p = float(input("percurso: "))
t = input("tipo: (A/B)")
if (t == "A"):
	pf = p / 8
	print(round(pf, 2))
elif (t == "B"):
	pf = p / 12
	print(round(pf, 2))