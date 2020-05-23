nota=float(input("nota do meliante:"))
boni= input("bonificacao? (S/N) ")
if (boni.upper()== "S"):
	print(round(nota*1.1,1))
else:
	print(round(nota,1))