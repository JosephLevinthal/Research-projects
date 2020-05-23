a = float(input("valor de compra:"))

if(a>200.00):
	x = a*0.05
	print(round(a-x,2))
else:
	print(round(a,2))
