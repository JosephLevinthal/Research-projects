a = int(input("valor a: "))
b = int(input("valor b: "))

p = a * b
r = p % 2

if r == 0:
	s = a + b
	print(s)
else:
	d = b - a
	print(d)