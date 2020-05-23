n=float(input("nota do aluno: "))
m=input("bonificacao: ")
if (m.upper()=="S"):
	n = n + n*(10/100)
	print(n)
else:
	print(n)
