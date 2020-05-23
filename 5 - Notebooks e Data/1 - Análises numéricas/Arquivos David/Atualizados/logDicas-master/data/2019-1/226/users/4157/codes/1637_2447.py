p = float(input("preco:"))
pg = float(input("pagamento:"))
if(p > pg):
   print("Falta",round(p-pg, 2))
else:
   print("Troco de",round(pg-p, 2))
	

	