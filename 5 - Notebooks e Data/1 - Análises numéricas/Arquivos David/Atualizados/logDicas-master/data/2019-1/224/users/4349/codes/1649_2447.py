num1= float(input("preco: "))
num2= float(input("pagamento: "))
						
if (num1>num2):
	x= num1-num2
	print("Falta", x)
else:
	y=num2-num1
	print("Troco de", y)