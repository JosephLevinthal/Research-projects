n = float(input("nota do aluno"))
opcao = input("bonificacao (S/N)")

if opcao.upper() == "S":
	nf = n * 1.1
else:
	nf = n
	
print(round(nf, 1))