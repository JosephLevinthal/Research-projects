a=float(input("nota do aluno: "))
n=input("bonificacao: ")
if (n.upper()=="S"):
	a = a + a*(10/100)
	print(a)
else:
	print(a)