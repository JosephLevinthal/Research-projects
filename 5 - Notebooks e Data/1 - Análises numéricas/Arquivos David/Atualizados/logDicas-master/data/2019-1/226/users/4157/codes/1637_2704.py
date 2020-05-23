n = float(input("nota do aluno:"))
b =input("vai receber bonificacao? (S/N)")
a = n*0.10
if(b.upper() == "S"):
	print(a + n)
else:
	print(n)