nota = float(input("Nota do Aluno: "))
bonus = input("Aluno recebera bonus? (S/N) ")

if (bonus.upper() == "N"):
	nota = nota
elif (bonus.upper() == "S"):
	nota = nota + (nota * 0.1)
else:
	print ("entrada invalida")
	
print (nota)