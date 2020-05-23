nota = float(input("Nota do aluno de 0 a 10:"))
opcao = input("Insira a abonificacao (S/N): ")

if (opcao.upper()) == "S":
	n = nota + (nota * 10/100)
	print (n)
else:
	print (nota)