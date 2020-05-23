pr = float(input("Preco: "))
pa = float(input("Pagamento: "))

if (pr > pa):
	falt= pr - pa
	print("Falta",round(falt,2))
else: 
	troc= pa - pr
	print("Troco de",round(troc,2))
