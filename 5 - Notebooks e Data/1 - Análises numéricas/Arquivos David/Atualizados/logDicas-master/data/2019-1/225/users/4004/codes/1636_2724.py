a = int(input("variavel a: "))
b = int(input("variavel b: "))
c = int(input("variavel c: "))

if a > b and a < c:
	print(a)
if a > c and a < b:
	print(a)
if b > a and b < c:
	print(b)
if b > c and b < a:
	print(b)
if c > a and c < b:
	print(c)
if c > b and c < a:
	print(c)