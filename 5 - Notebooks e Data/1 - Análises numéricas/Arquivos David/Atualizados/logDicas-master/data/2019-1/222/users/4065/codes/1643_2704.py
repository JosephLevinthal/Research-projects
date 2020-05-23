nota = float(input("nota do aluno: "))
aluno = input("S ou N: ")

if(aluno == "S"):
	print(nota + (nota * 10 / 100))
else:
	print(nota)
