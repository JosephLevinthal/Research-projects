nota = float(input("nota do aluno: "))
bonificacao = input("recebe bonificacao? (S/N)")

if (bonificacao.upper() == "S"):
	print(nota + (10/100 * nota))
	
else:
	print(nota)