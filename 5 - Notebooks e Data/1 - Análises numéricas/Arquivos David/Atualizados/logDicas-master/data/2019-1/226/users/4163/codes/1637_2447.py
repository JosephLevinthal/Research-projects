x = float(input("preco: "))
y = float(input("pagamento: "))

if (x > y):
	c = (x-y)
	print("Falta",round(c, 2))
else:
	c = (y-x)
	print("Troco de",round(c ,2))	