x=float(input("preco: "))
y=float(input("pagamento: "))

if(x>y):
	Falta= x-y
	print("Falta",round(Falta,2)) 
	
else:
	Troco= y-x
	print("Troco de",round(Troco,2))