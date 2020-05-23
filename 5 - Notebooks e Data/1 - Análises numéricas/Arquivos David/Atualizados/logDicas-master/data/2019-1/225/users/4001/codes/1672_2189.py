nome = input("Aluno(a): ")
if (nome[0].upper() >= "A") and (nome[0].upper() <= "K"):
	print(nome, "vai para a sala 101")
elif (nome[0].upper() >= "L" ) and (nome[0].upper() <= "N"):
	print(nome, "vai para a sala 102")
else:
	print(nome, "vai para a sala 103")