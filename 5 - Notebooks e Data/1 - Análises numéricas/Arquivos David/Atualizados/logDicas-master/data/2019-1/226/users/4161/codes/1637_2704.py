nota = float(input("nota do aluno: "))
extra = input("bonificacao? (S/N) ")
if (extra.upper() == "S"):
	print(round(nota*1.1, 1))
else:
	print(round(nota, 1))