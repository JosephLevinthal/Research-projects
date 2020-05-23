nota = float(input("insira a nota: "))
opcao = input("vai receber bonificacao? (S/N)")

if ( opcao.upper() == "S"):
	mensagem = nota + (nota * 10/100)
else:
	mensagem = nota
	
print(mensagem)