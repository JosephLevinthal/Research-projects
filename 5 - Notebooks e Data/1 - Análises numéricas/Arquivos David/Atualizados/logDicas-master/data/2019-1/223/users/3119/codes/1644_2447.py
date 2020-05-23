#Preco e pagamento
preco = float(input("Preco do produto: "))
pagamento = float(input("Pagamento: "))

X = round(preco - pagamento, 2)
Y = round(pagamento - preco, 2) 

if(preco > pagamento):
	print("Falta", X)
else:
	print("Troco de", Y)
	