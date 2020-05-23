a = int(input("Digite um numero a: "))
b = int(input("Digite um numero b: "))
c = int(input("Digite um numero c: "))
if(a < b < c):
	print(c)
if(c < b < a):
	print(a)
if(b < c < a):
	print(a)
if(b < a < c):
	print(c)
if(a < c < b):
	print(b)
if(c < a < b):
	print(b)