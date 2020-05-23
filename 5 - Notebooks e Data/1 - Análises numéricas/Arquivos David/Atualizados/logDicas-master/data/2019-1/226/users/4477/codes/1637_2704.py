nota = float(input("Determine a nota do fulano entre 0 e 10: "))
bonificacao = input("Determine S ou N: ")
					
if (bonificacao.upper() == "S"):
	acrescimo = (nota + (nota * 0.10))
else:
	acrescimo = nota
	
print(acrescimo)