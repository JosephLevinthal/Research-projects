nota_ini = float(input("nota do aluno:"))
bonus = input("aluno recebera a bonificacao?")

if bonus == 'S':
	nota_final = nota_ini*1.1
elif bonus == 'N':
	nota_final = nota_ini
	
print(round(nota_final, 1))
