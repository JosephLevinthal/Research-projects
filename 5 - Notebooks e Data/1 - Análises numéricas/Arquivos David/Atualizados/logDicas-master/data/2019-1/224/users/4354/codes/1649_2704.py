nota = float(input("nota do aluno: "))
bonificacao = input("recebe bonificacao? ")
bonificacao = bonificacao.lower()
if(bonificacao == "s") :
	nota = nota + (nota * 0.1)
	print(nota)
else :
	print(nota)
	  