pr = float(input("Preco: "))
pa = float(input("Pagamento: "))

if (pr > pa):
	x = pr - pa
	print("Falta ",x)
else:
	y = pa - pr
	print("Troco de ",y)