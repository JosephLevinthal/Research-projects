p= float(input("custo:"))
q= float(input("pago:"))

x= p-q
y= q-p

if(p > q):
	print("Falta",round(x,2))
else:
	print("Troco de",round(y,2))