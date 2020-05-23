#Notas dos alunos
nota = float(input("Nota do aluno: "))
mensagem = input("O aluno sera bonificado? ")

if(mensagem == "S"):
	print(nota + nota/10)
if(mensagem == "N"):
	print(nota)
