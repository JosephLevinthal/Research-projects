preco=float(input("digite o preco:"))
pagamento=float(input("digite o pagamento:"))
p1=(preco-pagamento)
p2=(pagamento-preco)
if(preco>pagamento):
	p="Falta"
	pp=p1
	print(p, round(pp,2))
else:
	t="Troco de"
	ppp=p2
	print(t,round(ppp,2))