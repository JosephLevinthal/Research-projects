preco = float(input("valor do preco"))
pag= float(input("valor pag"))
X = preco - pag
Y = pag - preco
if (preco > pag):
	print("Falta" , round(X,2))
	
else:
	print("Troco de" , round(Y,2))