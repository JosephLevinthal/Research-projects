a = int(input("1. Numero: "))
b = int(input("2. Numero: "))
c = int(input("3. Numero: "))

if(a > b > c or a > c > b ):
	print(a)

if(b > a > c or b > c > a):
	print(b)
	
if(c > a > b or c > b > a):
	print(c)
