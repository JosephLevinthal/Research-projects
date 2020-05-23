preco = float(input("preco e:"))
pagamento = float(input("pagamento e:"))
x = preco - pagamento
y = pagamento - preco
z = round(y,2)
if (preco > pagamento):
   print("Falta", x)
else:
	print("Troco de", z)
	