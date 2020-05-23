a = int(input("numero 1: "))
b = int(input("numero 2: "))
c = int(input("numero 3: "))

if (a>b>c or a>c>b):
	print(a)
if	(b>a>c or b>c>a):
   print(b)
if (c>a>b or c>b>a):
	print(c)