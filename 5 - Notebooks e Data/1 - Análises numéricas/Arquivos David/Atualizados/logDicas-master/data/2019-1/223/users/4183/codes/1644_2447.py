price = float(input("Digite o preco: "))
paid = float(input("Digite o pagamento: "))
X = price - paid
Y = paid - price
if (price > paid):
	print("Falta" , round(X,2))
else:
	print("Troco de" , round(Y,2))
	