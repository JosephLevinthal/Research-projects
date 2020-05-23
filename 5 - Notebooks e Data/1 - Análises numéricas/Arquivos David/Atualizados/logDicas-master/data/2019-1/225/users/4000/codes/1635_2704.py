nota = float(input("Digite a nota"))
boni =  (input(" bonificacao"))
if (boni == "S"):
	mensagem = nota + (10/100 * nota)
else:
	mensagem = nota
print(mensagem)
	
	