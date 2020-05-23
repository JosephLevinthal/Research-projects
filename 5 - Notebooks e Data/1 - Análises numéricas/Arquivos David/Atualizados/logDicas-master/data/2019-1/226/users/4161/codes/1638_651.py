altura = float(input("altura: "))
sexo = input("sexo (M/F): ")
pm = 72.7*altura - 58
pf = 62.1*altura - 44.7
if (sexo.upper() == "M"):
	print(round(pm, 2))
else:
	print(round(pf, 2))