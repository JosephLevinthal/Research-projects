pr = float(input("preco: "))
pa = float(input("pagamento: "))
tr = round(pa - pr ,2)
ft = round(pr - pa ,2)
if (pr > pa):
	print("Falta",ft)
else:
	print("Troco de",tr)