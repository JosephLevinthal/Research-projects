N=float(input("Qual a nota do aluno:? "))
M=input("Aluno vai receber a bonificacao:? S/N ")
if (M == "S"):
	print(N+N*10/100)
else:
	print(N)
	