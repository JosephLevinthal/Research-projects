a = int(input("numero qualquer:"))
b = int(input("numero:"))
c = int(input("numero:"))

if(a>b):
	if(b>c):
		print(c)
	else:
		print(b)
elif(b>a):
	if(a>c):
		print(c)
	else:
		print(a)
elif(c>a):
	if(a>b):
		print(b)
	else:
		print(a)