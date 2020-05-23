pr = float(input("preco do produto: "))
pa = float(input("quantia dada: "))

if (pr > pa):
	print("Falta",round(pr - pa,2))
	
	
else:	
	print("Troco de",round(pa - pr,2))
	

