p=float(input("preco: "))
pa=float(input("pagamento: "))
if(p>pa):
	a = p-pa
	print("Falta " ,round(a, 2))
else:
	b=pa-p
	print("Troco de " , round(b, 2))