preco = float(input("Qual o preco? "))
pagamento = float(input("Qual o pagamento?"))

x = preco - pagamento
y = pagamento - preco

if ( preco > pagamento ):
	print("Falta", x)
else:
	print("Troco de", y)
