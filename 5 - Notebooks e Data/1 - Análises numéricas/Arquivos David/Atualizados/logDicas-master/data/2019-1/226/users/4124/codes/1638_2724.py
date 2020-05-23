a = int(input("Digite um numero a: "))
b = int(input("Digite um numero b: "))
c = int(input("Digite um numero c: "))
if(a < b < c):
	print(b)
if(c < b < a):
	print(b)
if(b < c < a):
	print(c)
if(b < a < c):
	print(a)
if(a < c < b):
	print(c)
if(c < a < b):
	print(a)