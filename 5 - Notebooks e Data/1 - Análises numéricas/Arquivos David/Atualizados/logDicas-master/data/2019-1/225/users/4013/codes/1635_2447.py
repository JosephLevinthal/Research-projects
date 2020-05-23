p = float(input("preco:"))
pag = float(input("pagamento:"))
if (p > pag):
	print("Falta" , round((p - pag), 2))
else:
	print("Troco de" , round((pag - p), 2)) 