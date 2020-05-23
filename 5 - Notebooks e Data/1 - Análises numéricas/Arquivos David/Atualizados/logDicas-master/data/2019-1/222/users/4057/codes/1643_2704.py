n = float(input("Digite a nota do aluno de 0 a 10: "))
b = input("Aluno vai receber bonificacao ? (S/N)")

if (b.upper() == "S") :
	a = n * (10/100)
	print(n + a)
else :
	print(n)