p = float(input("preco: "))
pg = float(input("pagamento: "))
x = p - pg
z = round(x, 2)
y = pg - p
w = round(y, 2)

if (p > pg):
	msg = "Falta " + str(z)
else:
	msg = "Troco de " + str(w)
	
print(msg)