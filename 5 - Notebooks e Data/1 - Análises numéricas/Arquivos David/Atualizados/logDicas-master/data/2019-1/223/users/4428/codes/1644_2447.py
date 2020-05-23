preco = float(input("Digite o preco "))
pagamento = float(input("Digite o valor do pagamento: "))

x = round(preco - pagamento, 2)
y = round(pagamento - preco, 2)

if(preco > pagamento):
	print("Falta", x)
	
else:
	print("Troco de", y)
