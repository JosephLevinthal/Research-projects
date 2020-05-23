nota = float(input("nota do abencoado: "))
boni = input("bonificacao? (S/N) ")

if(boni.upper() == "S"):
	print(nota*1.1)
else:
	print(nota)