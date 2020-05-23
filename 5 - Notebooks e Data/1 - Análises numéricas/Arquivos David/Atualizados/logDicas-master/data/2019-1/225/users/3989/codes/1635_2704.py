nota_do_aluno = float(input("Digite nota:"))
bonificacao = input("Bonificacao? (S/N)")
pontoextra = 10/100

if (bonificacao == "S"):
	nota_final = nota_do_aluno + (nota_do_aluno * pontoextra)
else:
	nota_final = nota_do_aluno

print(nota_final)


	





	
