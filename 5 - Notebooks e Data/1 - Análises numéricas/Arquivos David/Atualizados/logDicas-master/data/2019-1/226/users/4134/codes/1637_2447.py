#Preço = a
#Pagamento = b

a = float(input("Preco sugerido: "))
b = float(input("Pagamento proposto: "))

if (a > b):
	x = a - b
	round(x, 2)
	msg = "Falta "
else: 
	x = b - a 
	round(x, 2)
	msg = "Troco de "
	
print(msg, x)	