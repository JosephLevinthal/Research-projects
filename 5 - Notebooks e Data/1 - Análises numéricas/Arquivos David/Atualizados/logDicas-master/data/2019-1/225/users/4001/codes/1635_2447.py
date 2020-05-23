a = float(input("Preco: "))
b = float(input("Pagamento: "))
X = a - b
Y = b - a

if (a > b):
	print("Falta ", round(X, 2))
else:
	print("Troco de ", round(Y, 2))

	
	
