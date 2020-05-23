nota = float(input("Nota do aluno:"))
bonificacao = input("bonificacao?:")
if(bonificacao.upper()=="S"):
	notafinal = nota + (nota*0.1)
	print(notafinal)
else:
	print(nota)