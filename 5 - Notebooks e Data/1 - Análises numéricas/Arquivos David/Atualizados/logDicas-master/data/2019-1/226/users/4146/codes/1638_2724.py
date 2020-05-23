a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if (a>b>c):
	print(b)
else:
	d = (c>b>a)
	print(b)

if (b>a>c):
	print(a)
else:
	e = (c>a>b)
	print(a)

if (a>c>b):
	print(c)
else:
	f = (b>c>a)
	print(c)