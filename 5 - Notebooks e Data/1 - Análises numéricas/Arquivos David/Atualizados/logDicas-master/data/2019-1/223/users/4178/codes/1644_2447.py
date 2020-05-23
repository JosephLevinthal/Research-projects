var1= float(input("Preco: "))
var2= float(input("Valor pago : "))

if var1 > var2 :
	print("Falta",  float(round(var1 - var2)))
else:
	print("Troco de ", float(round(var2 - var1)))