num= float(input("preco: "))
num2= float(input("pagamento: "))
x= num-num2
y = num2-num

if (num > num2):
	print("Falta" ,round(x,2))
else:
	print("Troco de" , round(y,2))