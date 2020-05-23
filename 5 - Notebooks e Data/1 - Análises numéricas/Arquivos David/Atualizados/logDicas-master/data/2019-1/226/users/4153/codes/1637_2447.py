preco = float(input("Insira o preco: "))
pagamento = float(input("Insira o valor do pagamento: "))

x = preco - pagamento
y = pagamento - preco

if(preco > pagamento):
	msg = x
	print("Falta ", round(x,2))
else:
	msg = y
	print("Troco de ", round(y,2))
