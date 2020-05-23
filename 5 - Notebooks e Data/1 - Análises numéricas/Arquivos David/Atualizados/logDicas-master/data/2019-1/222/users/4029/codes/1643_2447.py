pc= float(input("Digite o perco: "))
pg= float(input("Digite o pagamento: "))
if (pc > pg):
	a= (pc-pg)
	print("Falta {}".format(round(a, 2)))
else:
	a= (pg-pc)
	print("Troco de {}".format(round(a, 2)))