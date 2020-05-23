a= float(input("area fertilizada: "))
if(a<=10000):
	print(round(a*5, 2))
else:
	e=a-10000
	print(round(5*10000+e*4, 2))