x = float(input("preco:"))
y =float(input("pagamento:"))

s = x - y
troco = (y - x)
e = round(troco, 2)
if (x > y):
	print ("Falta", s)
	
else:
	print("Troco de", e)
	