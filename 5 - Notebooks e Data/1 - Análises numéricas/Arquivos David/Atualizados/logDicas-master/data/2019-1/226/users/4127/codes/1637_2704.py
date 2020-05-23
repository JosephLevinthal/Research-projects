nota = float(input("qual a nota do aluno? "))
bb= input("o aluno recebera bonificacao?(S ou N) ")

notaB= nota+(nota*0.10)

if (bb.upper()== "S"):
	msg= notaB
else:
	msg= nota
print(msg)
