preco = float(input("preco:"))
pagamento = float(input("pagamento: "))
x = pagamento - preco
y = preco - pagamento
if(preco > pagamento):
	print("Falta", y)
else:
	print("Troco de", x)
