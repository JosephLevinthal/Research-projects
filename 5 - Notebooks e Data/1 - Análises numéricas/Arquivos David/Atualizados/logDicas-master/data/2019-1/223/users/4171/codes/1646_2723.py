a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a < b:
	if b < c:
		print(c)
	else:
		print(b)
else:
	if a < c:
		print(c)
	else:
		print(a)