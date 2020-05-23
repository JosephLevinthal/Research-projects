x = float(input("Nota do aluno: "))
b = input("Receber bonificacao (S / N): ")

if (b == "S"):
	mensagem = x + (x * (10/100))
else:
	mensagem = x
		
print(mensagem)