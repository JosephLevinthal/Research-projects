a = float(input("Preco a pagar: "))
b = float(input("Pagamento:"))
if ( a > b):
	eq = a - b
	round(eq,2)
	mgs = "Falta "
else: 
	eq = b - a
	round(eq,2)
	mgs = "Troco de "
print(mgs,eq)