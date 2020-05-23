nota=float(input("Nota do aluno: " ))
opcao = input("Ira receber bonificacao? (S/N) ")
				 
if (opcao.upper() == "S"):
	total = nota + nota*10/100
				 
else:
	total = nota
print(round(total, 2))