pr= float(input("preco :"))
pag= float(input("pagamento: "))

if ( pr > pag) :
	x= pr - pag 
	print("Falta ", x)
	
else : 
	y= pag - pr
	print("Troco de ", y)
	