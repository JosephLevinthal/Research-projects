a=float(input("num1    "))
b=float(input("num2    "))
c=float(input("num3    "))
if(c<a<b):
		print(a)
else:
	if(b<a<c):
		print(a)
	else:
		if(a<b<c):
			print(b)
		else:
			if(c<b<a):
				print(b)
			else:
				print(c)
