a = float(input("number a: "))
b = float(input("number b: "))
c = float(input("number c: "))

if a < b and a < c:
	print(a)
if b < a and b < c:
	print(b)
if c < a and c < b:
	print(c)