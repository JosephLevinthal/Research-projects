pr= float(input("insira o preco: "))
pag=float(input("insira o pagamento: "))
l= pr-pag
t=pag-pr
if pr>pag:
	print('Falta', l)
else:
	print('Troco de', t)

