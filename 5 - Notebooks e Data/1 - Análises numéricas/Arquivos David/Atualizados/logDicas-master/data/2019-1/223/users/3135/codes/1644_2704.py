#Nota do aluno
N= float(input("Insira a nota do aluno"))
#Opção
O= input("Insira se o aluno vai receber ou nao.(S/N)")

if (O == "S"):
	Nf= N + N* (10/100)
else:
	Nf= N

print(Nf)