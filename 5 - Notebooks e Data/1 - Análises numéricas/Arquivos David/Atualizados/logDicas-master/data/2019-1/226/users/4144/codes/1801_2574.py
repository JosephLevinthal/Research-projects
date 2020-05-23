n = input("digite a senha: ")
for i in len(n):
	if(len(n)>=8):
		if(n.islower()):
			if(n.isupper()):
				print("SENHA VALIDA")
			else:
				print("SENHA INVALIDA")