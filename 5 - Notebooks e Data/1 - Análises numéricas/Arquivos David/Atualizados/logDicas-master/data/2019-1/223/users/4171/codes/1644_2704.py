a = float(input("nota do aluno: "))
b = input("bonificacao? (S/N) ")

if (b.upper() == "S"):
	print(float(a + a * 0.1))
else:
	print(float(a))