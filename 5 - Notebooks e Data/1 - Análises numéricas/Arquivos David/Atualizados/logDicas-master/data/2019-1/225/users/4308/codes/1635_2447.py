pr= float(input("preco :"))
pag= float(input("pagamento: "))
if ( pr > pag ) :
	x= pr - pag
	print("Falta ",round(x, 2))
else :
	y= pag - pr
   print("Troco de ",round(y, 2))
	