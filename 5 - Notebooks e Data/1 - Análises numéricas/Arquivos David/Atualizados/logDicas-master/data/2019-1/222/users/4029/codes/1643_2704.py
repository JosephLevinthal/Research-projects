x= float(input("Nota do aluno: "))
y= input("O aluno ira receber bonificacao? (S/N) ")
if (y == "S"):
	nota= x + (x/10)
else:
	nota= x
print(round(nota, 2))