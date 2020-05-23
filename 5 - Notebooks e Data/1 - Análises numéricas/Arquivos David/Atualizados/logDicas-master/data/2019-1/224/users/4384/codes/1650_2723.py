a=float(input("num1    "))
b=float(input("num2    "))
c=float(input("num3    "))
if(a>b):
	if(a>c):
		print(a)
	else:
		if(b>a):
			if(b>c):
				print(b)
			else:
				if(c>a):
					if(c>b):
						print(c)
		else:
			if(c>a):
				if(c>b):
					print(c)
else:
		if(b>a):
			if(b>c):
				print(b)
			else:
				if(c>a):
					if(c>b):
						print(c)	
		else:
			if(c>a):
				if(c>b):
					print(c)