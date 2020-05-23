n = float(input("Nota do aluno: "))
m = input("Vai receber a bonificacao: ")
if (m == "S"):
	a = n + (n*10/100)
	print(a)
else:
	print(n)
