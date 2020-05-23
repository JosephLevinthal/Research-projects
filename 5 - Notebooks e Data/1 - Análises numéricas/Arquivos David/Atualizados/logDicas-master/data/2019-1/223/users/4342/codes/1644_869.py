var=float(input("preco sem desconto:"))

desconto= (var*(5/100))

if (var < 200):
	print(var)
if (var >= 200):
	print(round(var-desconto, 2))
	