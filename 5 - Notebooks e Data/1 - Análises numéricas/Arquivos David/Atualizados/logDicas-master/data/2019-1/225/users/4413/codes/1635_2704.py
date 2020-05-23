nota = float(input("nota: "))
bonificacao = input("bonificacao: ")
if(bonificacao=="S"):
	mensagem = (nota+nota*10/100)
else:
	mensagem = (nota)
print(mensagem)