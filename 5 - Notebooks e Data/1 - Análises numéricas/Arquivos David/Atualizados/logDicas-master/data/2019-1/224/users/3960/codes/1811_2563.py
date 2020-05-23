from numpy import *

medias = array(eval(input("Insira as medias finais dos alunos: ")))

while(len(medias) > 1):
	aprovados = 0

	for x in medias:
		if(5 <= x < 7):
			aprovados += 1
	
	print(aprovados)
	
	medias = array(eval(input("Insira as medias finais dos alunos: ")))