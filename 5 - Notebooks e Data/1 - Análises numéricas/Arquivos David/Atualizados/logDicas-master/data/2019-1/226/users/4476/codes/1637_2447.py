preco = float(input("digite o preco: "))
pagamento = float(input("digite o pagamento: "))

x =  preco -pagamento
y = pagamento- preco 

if (preco > pagamento):
	msg = x
	print("Falta ", round(x, 2))
	
else:
	msg = y
	print("Troco de ", round(y, 2))	