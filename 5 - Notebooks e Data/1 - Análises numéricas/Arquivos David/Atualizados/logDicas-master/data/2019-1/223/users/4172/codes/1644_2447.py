p=float(input("preco: "))
pa=float(input("pagamento: "))
y = p - pa
z = pa - p
if p > pa:
	x = "Falta" +" "+ str(y)
else:
	x = "Troco de" +" "+ str(z)
print(x)