nota = float(input("nota: "))
boni = input("boni: ")
if boni.upper() == "S":
	mensagem = nota + (10/100* nota)
else:
	mensagem = nota
print(mensagem)