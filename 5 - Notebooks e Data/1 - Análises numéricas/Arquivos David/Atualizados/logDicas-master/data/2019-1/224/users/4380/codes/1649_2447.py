preco= float(input("preco da compra: "))
pag= float(input("pagamento da compra: "))
x=float(round(preco-pag,2))
y=float(round(pag-preco,2))
if (preco > pag):
	print("Falta ", x)
else:
	print("Troco de ", y)
