x=float(input("preco: "))
y=float(input("pagamento: "))
if(x>y):
	a=x-y
	print("Falta",a)
else:
	b=y-x	
	print("Troco de",b)