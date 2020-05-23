n = float(input("nota do aluno: "))
op = input("bonificacao  (S/N) : ")
if (op.upper() == "S") :
	Y = (n * 0.1) + n
	print(float(Y))
else :
	print(float(n))