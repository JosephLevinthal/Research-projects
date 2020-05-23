n1 = int(input("Insira o numero: "))
n2 = int(input("Insira o numero: "))

s = n1 + n2
d = n2 - n1

if((n1 * n2) % 2 == 0):
	print(s)
else:
	print(d)