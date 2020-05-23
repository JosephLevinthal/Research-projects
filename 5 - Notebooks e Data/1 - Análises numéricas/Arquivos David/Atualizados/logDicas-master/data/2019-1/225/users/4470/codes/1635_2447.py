preco = float(input())
pagamento = float(input())
X = preco - pagamento
Y = pagamento - preco
if (preco>pagamento):
	print("Falta ",round(X, 2))
	
else: 
	print("Troco de ",round(Y, 2))
