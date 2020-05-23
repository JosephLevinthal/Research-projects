nota = float(input("nota do aluno:"))
acrescimo = input("o aluno ira receber o acrescimo de 10%? (S/N)")
if (acrescimo.upper() == "N"):
	print(nota)
else:
	nf= nota + (nota*10/100)
	print(nf)
