a = int(input("numero1: "))
b = int(input("numero2: "))
c = int(input("numero3: "))
if (a>b>c):
	print(c)
if (a>c>b):
	print(b)
if (b>c>a):
	print(a)
if (b>a>c):
	print(c)
if (c>b>a):
	print(a)
if (c>a>b):
	print(b)