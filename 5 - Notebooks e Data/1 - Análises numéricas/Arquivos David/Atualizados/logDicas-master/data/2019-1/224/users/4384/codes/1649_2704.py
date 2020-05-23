nota=float(input("nota de zero a dez:    "))
bonificacao=input("recebera bonificacao:?    (S/N) ")
if(bonificacao.upper()=="S"):
	x=nota+nota*0.1
	print(x)
else:
	if(bonificacao.upper()=="N"):
		print(nota)