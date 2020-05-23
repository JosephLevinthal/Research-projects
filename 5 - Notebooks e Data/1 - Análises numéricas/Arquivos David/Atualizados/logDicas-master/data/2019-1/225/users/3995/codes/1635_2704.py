n=float(input("nota do aluno: "))
l=input("var receber bonificacao? S/N")
if(l=="S"):
	n=(n+(n*0.1))
else:
	n=n
print(n)