x=float(input("valor de x: "))
if(x<=1):
	print(round(1, 2))
elif((x>1)and(x<=2)):
	print(round(2, 2))
elif((x>2)and(x<=3)):
	print(round(x**2, 2))
elif((x>3)):
	print(round(x**3, 2))
		  