n =int(input("numero1: "))
n1 =int(input("numero2: "))
n2 =int(input("numero3: "))

if(n > n1 > n2):
	print(n1)
if(n1 > n > n2):
	print(n)
if(n2 > n1 > n):
	print(n1)
if(n1 > n2 > n):
	print(n2)
if(n > n2 > n1):
	print(n2)
if(n2 > n > n1):
	print(n)