p=float(input("preco:"))
pag=float(input("pagamento:"))
x= p - pag
y= pag - p
if (p > pag):
	print("Falta", x)
else:
	print("Troco de", y)