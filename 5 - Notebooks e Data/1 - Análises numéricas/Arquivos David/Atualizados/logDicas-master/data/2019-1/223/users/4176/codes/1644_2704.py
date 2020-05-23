nota= float(input('Nota do aluno: '))
condicao= input("Bonificacao: ")


if (condicao == "S"):

	formula = (nota + (nota * 0.1))
	print(formula)
	
else:
	print(nota)




