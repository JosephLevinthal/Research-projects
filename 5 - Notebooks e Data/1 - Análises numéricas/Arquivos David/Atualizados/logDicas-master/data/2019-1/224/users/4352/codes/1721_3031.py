x = float(input("digite x: "))
fx1 = 1
fx2 = 2
fx3 = round(x**2, 2)
fx4 = round(x**3, 2)
if x<=1:
	print(fx1)
elif x>1 and x<=2:
	print(fx2)
elif x>2 and x<=3:
	print(fx3)
elif x>3:
	print(fx4)