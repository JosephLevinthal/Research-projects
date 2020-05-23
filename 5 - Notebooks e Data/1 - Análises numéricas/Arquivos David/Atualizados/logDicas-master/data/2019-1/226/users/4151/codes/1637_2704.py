x=float(input(" nota do aluno: "))
y=input("bonificacao: (S ou N)")

if(y.upper()=="S"):
	print(x+(x*0.10))
else:
	print(x)
	