#Digitar a nota do aluno
nota=float(input("Qual foi a nota do aluno? "))

#receberar bonus S/N
bonus=input("vai rereceber o bonus, S/N?: ")

#condicao
if (bonus=="S"):
	mensagem = nota + nota*(10/100)

else:
	mensagem = nota

#impressao da nota
print(mensagem)