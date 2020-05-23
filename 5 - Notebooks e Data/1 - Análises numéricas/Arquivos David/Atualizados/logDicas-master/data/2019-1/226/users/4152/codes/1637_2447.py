p1 = float(input("Digite aqui o preco: "))

p2 = float(input("Digite aqui o valor do pagamento: "))

X = p1 - p2

Y = p2 - p1

if (p2 >= p1):
	print("Troco de" , Y)
else:
	print("Falta" , X)