x = float(input("Valor de x:"))

if(x <= 1):
	print(1)
elif( 1 < x and x <=2):
	print(2)
elif(2 < x and x <= 3):
	z = x**2
	print(round(z, 2))
elif(x > 3):
	z = x**3
	print(round(z, 2))