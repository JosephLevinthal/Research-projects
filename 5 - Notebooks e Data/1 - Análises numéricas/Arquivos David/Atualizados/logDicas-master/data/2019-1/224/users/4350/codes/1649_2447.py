a = float(input("preco"))
b = float(input("pagamento"))
if a > b:
	print("Falta", round(a - b, 2))
if b >= a:
	print("Troco de", round(b - a, 2))