x = float(input("qual o valor de x? "))
if(x <= 1):
	print(1)
elif(1 < x <= 2):
	print (2)
elif(2 < x <= 3):
	print(round(x ** 2, 2))
elif(x > 3):
	print(round(x ** 3, 2))