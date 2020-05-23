a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b:
	if b > c:
		print(b)
	else:
		print(c)
else:
	if a > c:
		print(a)
	else:
		print(b)