n1 = int(input("insira o numero1: "))
n2 = int(input("insira o numero2: "))
n3 = int(input("insira o numero3: "))

if(n1 > n2 > n3):
	print(n1)
if(n1 > n3 > n2):
	print(n1)
if(n2 > n3 > n1):
	print(n2)
if(n2 > n1 > n3):
	print(n2)
if(n3 > n2 >n1):
	print(n3)
if(n3 > n1 > n2):
	print(n3)