nota = float(input("nota do aluno: "))
boni = input("aluno com bonificacao: (S/N) ")

if(boni.upper()=="S"):
	nota = nota*0.1+nota
else:
	nota = nota
print(nota)