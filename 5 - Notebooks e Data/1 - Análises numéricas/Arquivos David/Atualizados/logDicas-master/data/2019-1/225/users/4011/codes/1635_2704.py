n = float(input("Qual a nota do aluno? "))
b = input("o aluno recebera a bonificacao (S/N)? ")

if (b.upper() == "S"):
	nota = n + (n/10)
else:
	nota = n

print(nota)