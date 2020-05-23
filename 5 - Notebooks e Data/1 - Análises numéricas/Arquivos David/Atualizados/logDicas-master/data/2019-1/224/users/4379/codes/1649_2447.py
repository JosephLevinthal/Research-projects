preco=float(input("digite o preco: "))
pag=float(input("digite o pagamento: "))
x= preco - pag
y= pag - preco
if preco > pag:
    print("Falta" , x)
else:
	print("Troco de" , y)