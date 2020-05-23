n = float(input("Nota do aluno: "))
b = input("Bonifacao: ")

if (b.upper() == "S"):
	print(n + (n * 0.10))
else:
	print(n)