nota = float(input("nota 0 a 10: "))
bonificacao = input("Bonificacao? (S/N)   ")

if (bonificacao.upper() == "S"):
	print(nota + nota*(10/100))
	
else:
	print(nota)
	
