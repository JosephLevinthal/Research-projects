nota= float(input("nota do aluno: "))
bon= input("o aluno tem bonificacao: ")
if bon.upper()=="S":
	print(nota + 10/100 * nota)
else:
	print(nota)