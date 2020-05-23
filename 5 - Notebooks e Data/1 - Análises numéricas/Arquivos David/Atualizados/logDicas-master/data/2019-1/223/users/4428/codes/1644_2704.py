nota_inicial = float(input("Digite nota do aluno: "))
bonificacao = input("Aluno recebera bonificacao: ")

acrescimo = ((nota_inicial/100)*10)

if(bonificacao == "S"):
	nota_final = nota_inicial + acrescimo
else:
	nota_final = nota_inicial

print(nota_final)