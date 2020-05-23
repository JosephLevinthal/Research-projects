preço = float(input("digite o golpe: "))
pagamento = float(input("digite as lagrimas: "))
x = preço - pagamento
y = pagamento - preço
if preço > pagamento:
	c = "Falta"
	d = x
	print(c, round(d, 2))
else:
	a = "Troco de"
	b = y
	print(a, round(b, 2))