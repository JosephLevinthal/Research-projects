nota = float(input("nota do aluno e: "))
mensagem = input("bonificacao (S/N)")

if (mensagem.upper() == "S"):
	a = nota + (nota * 10/100)
	print(a)
else:
	print(nota)