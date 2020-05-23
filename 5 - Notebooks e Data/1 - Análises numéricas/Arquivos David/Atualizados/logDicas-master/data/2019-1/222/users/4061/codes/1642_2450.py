nome1 = input("digite nome 1: ")
nome2 = input("digite nome 2: ")

if(nome1.upper() < nome2.upper()):
	mensagem1 = nome1
	mensagem2 = nome2
else:
	mensagem1 = nome2
	mensagem2 = nome1
	
print(mensagem1)
print(mensagem2)