nota = float(input("valor da nota? "))
aluno_bonificado = input(" S ou N? ")
s = nota * 10 / 100
valor_final = nota + s
bonus = ("S")
if (aluno_bonificado == bonus):
	print(valor_final)
else:
	print(nota)