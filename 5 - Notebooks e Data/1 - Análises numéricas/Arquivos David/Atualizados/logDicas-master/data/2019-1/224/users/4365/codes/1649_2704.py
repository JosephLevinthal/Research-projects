nota= float(input("nota do aluno:"))
boni=input("o aluno tem bonificacao :")
if boni.upper()== "S":
	print(nota + 10/100 * nota)
else:
	print(nota)


	