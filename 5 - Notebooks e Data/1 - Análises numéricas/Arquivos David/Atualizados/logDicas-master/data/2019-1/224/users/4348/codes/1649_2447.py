a=float(input("digite o preco:"))
b=float(input("pagamento:"))
if( a > b):
	eq = a - b
	round(eq,2)
	msg="Falta "
else:
	eq = b - a
	round(eq,2)
	msg="Troco de "
print(msg,eq)