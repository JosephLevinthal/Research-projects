x = float(input("digite x: "))
if (x <= 1):
	f = 1  
	print(round(f, 2))
elif (1 < x and x <= 2):
	f = 2
	print(round(f, 2))
elif (2 < x and x <= 3):
	f = x ** 2
	print(round(f ,2))
elif ( x > 3):
	f = x ** 3
	print(round(f, 2))