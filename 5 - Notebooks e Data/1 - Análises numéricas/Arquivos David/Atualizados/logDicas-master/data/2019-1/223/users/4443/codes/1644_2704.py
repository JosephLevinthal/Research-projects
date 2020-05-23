#Leitura da nota do aluno
nota = float(input("Digite a nota do aluno: "))
bonus = input("O aluno vai receber bonificacao? ")

#Calculo da nota:
if (bonus == "S"):
	nf = nota * 1.10
	print(nf)
else: 
	print(nota)