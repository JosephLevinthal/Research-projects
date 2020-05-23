nota = float(input("Nota do aluno: "))
boni = input("S ou N: ")

if (boni.upper() == "S"):
	aumento = nota*0.1
	mensagem = nota + aumento
else:
	mensagem = nota
	
print(mensagem)	