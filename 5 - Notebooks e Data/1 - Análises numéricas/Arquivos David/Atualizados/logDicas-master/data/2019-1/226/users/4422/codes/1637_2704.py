nota = float(input("Qual a nota: "))
bonificacao = input("Vai receber bonificacao? (S/N)")
if(bonificacao.upper() == "S"):
	mensagem = nota + (nota*10/100)

else:
	mensagem = nota
	
print(mensagem)
