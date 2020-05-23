preco= float(input(""))
pag= float(input(""))
if (preco>pag):
	x= preco-pag
	print("Falta", round(x,2))
	
else:
	y=pag-preco
	print("Troco de", round(y,2))