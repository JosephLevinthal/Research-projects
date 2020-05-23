nota_do_aluno= float(input("digite a nota:"))
mensagem= input("digite S ou N : ")
mensagem= mensagem.upper()
if(mensagem=="S"):
	nota_do_aluno = nota_do_aluno+(nota_do_aluno*10/100)
	print(nota_do_aluno)
if(mensagem=="N"):
	nota_do_aluno = nota_do_aluno
	print(nota_do_aluno)
	