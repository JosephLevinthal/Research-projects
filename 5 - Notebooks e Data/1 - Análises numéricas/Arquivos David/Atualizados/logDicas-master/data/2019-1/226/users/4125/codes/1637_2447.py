n = float(input("digite o preco:"))
n1 = float(input("digite o pagamento: "))
if (n>n1):
	x = n-n1
	print("Falta", round(x,2))
else:
	x = n1-n
	print("Troco de", round(x,2))