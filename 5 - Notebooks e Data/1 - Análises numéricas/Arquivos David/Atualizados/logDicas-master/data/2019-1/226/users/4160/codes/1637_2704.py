nota = float(input("Digite a nota do aluno: "))
mensagem = input ("Bonificacao ou nao (S ou N): ")

if (mensagem == "S") :
	final = nota + (nota * 0.1)
else: 
	final = nota
	
print(final)