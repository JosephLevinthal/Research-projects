n = float(input("nota do aluno"))
b = input("bonificacao (S/N)")

if (b.upper()== "S"):
   nf = n + (10 / 100 * n)
else:	
	nf = n
print(nf)	
	

	
	