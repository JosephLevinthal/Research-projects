bonificacao=input("recebera bonificacao:?   (S/N) ")
preco=float(input("valor do ing:   "))
ingressos=int(input("qtd de ing:   "))
if(bonificacao.upper()=="S"):
	x=preco+preco*0.2
	print(round(x))
else:
	if(bonificacao.upper()=="N"):
		print(round(bonificacao))