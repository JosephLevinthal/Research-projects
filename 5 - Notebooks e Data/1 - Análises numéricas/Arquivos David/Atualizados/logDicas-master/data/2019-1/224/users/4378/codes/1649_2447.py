preco= float(input("preco:"))
pag= float(input("pagamento:"))
x= preco - pag
y= pag - preco
if (preco > pag):
	print("Falta", x)
else:
	print("Troco de", y)