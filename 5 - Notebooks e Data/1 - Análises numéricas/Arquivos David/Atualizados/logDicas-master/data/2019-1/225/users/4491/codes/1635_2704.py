nota = float(input("nota: "))
opcao = input("bonificacao? (S/N) ")

if (opcao.upper() == "S"):
	n = nota + (nota * 10 / 100)
	print(n)
else: 
	print(nota)

