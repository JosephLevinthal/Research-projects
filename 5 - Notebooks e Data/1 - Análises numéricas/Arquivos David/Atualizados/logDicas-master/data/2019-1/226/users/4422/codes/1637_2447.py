preco = float(input("Qual o preco: "))
pagamento = float(input("Valor pago: "))

if(preco > pagamento):
	print("Falta", round(preco - pagamento, 2))
	
else:
	print("Troco de ", round(pagamento - preco, 2))
	
