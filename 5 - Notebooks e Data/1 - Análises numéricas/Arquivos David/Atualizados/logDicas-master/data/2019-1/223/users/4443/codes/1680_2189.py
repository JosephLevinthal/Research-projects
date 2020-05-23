# Coleta do nome dos estudantes:
nome = input("Digite o nome do estudante: ")

pri = nome[0].upper()
fim = nome[1:]

if ("A" <= nome <= "K"):
	print(pri+fim, "vai para a sala 101")
elif ("L" <= nome <= "N"):	
	print(pri+fim, "vai para a sala 102")
else:	
	print(pri+fim, "vai para a sala 103")