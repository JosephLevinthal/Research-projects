n1 = int(input("insira o numero1: "))
n2 = int(input("insira o numero2: "))

s = n1 + n2
d = n2 - n1

if ((n1  * n2) % 2 == 0):
	print(s)
else:
	print(d)