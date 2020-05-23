nota = float(input("nota: "))
bonificacao = input("s ou n")

if(bonificacao == "S"):
	notafinal = nota + nota*0.10
	print(notafinal)
else:
	notafinal = nota
	print(notafinal)