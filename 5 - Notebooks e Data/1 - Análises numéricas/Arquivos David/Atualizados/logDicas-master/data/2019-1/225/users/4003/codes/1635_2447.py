x = float(input("preco: "))
y = float(input("pagamento: "))

troco = y - x
dif = x - y
if(x > y):
	print("Falta", round(dif,2))
else:
	print("Troco de", round(troco,2))
	