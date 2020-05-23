nota =float(input("Digite uma nota de 0 a 10: "))
bonificacao =input("Digite S ou N: ")
if(bonificacao == "S"):
	acrescimo = nota + ((nota * 10) /100)
	print(acrescimo)
else:
	print(nota)
	
	