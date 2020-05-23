x = float(input("valor de x e:"))

if(x <= 1):
	u = round(1,2)
	print(u)
elif(x > 1) and (x <= 2):
	d = round(2,2)
	print(d)
elif(x > 2) and (x <= 3):
	e = round(x**2, 2)
	print(e)
elif(x > 3):
	f = round(x**3,2)
	print(f)
