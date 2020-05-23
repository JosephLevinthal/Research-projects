n= float(input("nota do aluno: "))
op= input("bonificacao  (S/N) : ") 
if (op.upper() == "S") :
	y= (n * 0.1) + n
	print(y)

else :
	print(n)