preco= float(input("Preco:"))
pag= float(input("Pagamento:"))
p= preco - pag
f= pag - preco
if (preco > pag):
	print("Falta ", round(p, 2))
else:
	print("Troco de ", round(f, 2))
