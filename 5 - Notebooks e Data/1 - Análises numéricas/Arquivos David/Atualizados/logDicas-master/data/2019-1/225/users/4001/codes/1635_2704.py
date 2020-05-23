nota = float(input("Nota do aluno: "))
opcao = input("Bonificacao? (S/N) ")
if (opcao.upper() == "S"):
	nota = nota + (nota * 10/100)
print(nota)
	