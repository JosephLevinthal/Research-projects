preco = float(input("Digite o preco: "))
pagamento = float(input("Digite o pagamento: "))
p1 = (preco - pagamento)
p2 = (pagamento - preco)
if(preco > pagamento):
	p = "Falta"
	pp = p1
	print(p, round(pp, 2))
else:
	t = "Troco de"
	tt = p2
	print(t, round(tt, 2))
	