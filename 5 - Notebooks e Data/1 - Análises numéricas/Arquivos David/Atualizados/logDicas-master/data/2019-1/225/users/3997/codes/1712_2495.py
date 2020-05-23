nmr = int(input("Digite um numero: "))

while (nmr!=-1):
	if (nmr % 2==0):
		mensagem = ("PAR")
	else:
		mensagem = ("IMPAR")
	
	print(mensagem)
	nmr = int(input("Digite um numero: "))
