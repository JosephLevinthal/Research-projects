nota = float(input("digite nota: "))
boni = input("S ou N: ")

if(boni == "S" ):
	mensagem = nota+(nota*0.10)
else:
	mensagem = (nota)

print(mensagem)