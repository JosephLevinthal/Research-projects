x = float(input("Insira o valor de x: "))

if(x <= 1):
	f = 1
elif(1 < x <= 2):
	f = 2
elif(2 < x <= 3):
	f = x ** 2
elif(x > 3):
	f = x ** 3
print(round(f, 2))