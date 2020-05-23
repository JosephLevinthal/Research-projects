a = int(input("1. Numero: "))
b = int(input("2. Numero: "))
c = int(input("3. Numero: "))

d1 = a > b
d2 = b > c
d3 = a > c

if(a < b < c or c < b < a ):
	print(b)

if(b < a < c or c < a < b):
	print(a)
	
if(a < c < b or b < c < a):
	print(c)
