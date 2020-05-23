cliente = float(input("Taxa de pagamento: "))

if cliente ><10
	vc = 30.00 + (3.00 * cliente)
else:
	vc = 30.00 + (3.50 * cliente)
	
print(round(vc, 2))