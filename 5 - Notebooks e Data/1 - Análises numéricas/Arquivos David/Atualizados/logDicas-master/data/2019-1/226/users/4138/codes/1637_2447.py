x = float(input("insira o preco: "))
y = float(input("insira o pagamento: "))

X = x - y
Y = y - x

if ( x > y):
	mensagem = X
	print("Falta", round(X,2))
else:
	mensagem = Y
	print("Troco de ", round(Y,2))
	
	
