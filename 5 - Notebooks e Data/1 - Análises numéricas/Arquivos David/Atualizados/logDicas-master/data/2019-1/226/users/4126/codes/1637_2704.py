nota= float(input("aluno:"))
bon= input("bonificacao:")

nota1= nota + (nota/10)
nota2= nota

if (bon== "S"):
	print(round(nota1,2))
else:
	print(round(nota2,2))