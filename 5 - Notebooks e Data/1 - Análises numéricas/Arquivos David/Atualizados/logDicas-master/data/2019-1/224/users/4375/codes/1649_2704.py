nota=float(input("digite uma nota: "))
bonificacao=input("bonificacao S ou N: ")
bonificacao=bonificacao.upper()
if bonificacao=="S":
	mensagem= nota + nota*10/100
	print(mensagem)
else:
	print(nota)