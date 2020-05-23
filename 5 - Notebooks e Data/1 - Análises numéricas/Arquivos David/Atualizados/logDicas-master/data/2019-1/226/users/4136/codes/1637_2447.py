var1 = float(input("informe o preco: "))
var2 = float(input("informe o pagamento: "))
var3 = var1 - var2
var4 = var2 - var1

if (var2 < var1):
	print("Falta", var3) 
else:
	print("Troco de", var4)
