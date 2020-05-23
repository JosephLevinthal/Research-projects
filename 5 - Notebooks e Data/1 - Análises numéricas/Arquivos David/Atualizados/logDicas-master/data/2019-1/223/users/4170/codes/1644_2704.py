nota = float(input("Nota do aluno: "))
mensagem = input("Mensagem: ")
acrescimo = (nota*10)/100
if (mensagem == "S"):
	nota_final = nota + acrescimo
	print(nota_final)
else:
	nota_final = nota
	print(nota_final)