n1 = int(input("numero1: "))
n2 = int(input("numero2: "))

if (n1 * n2) % 2 == 0:
	print(n1 + n2)
else:
	print(abs(n1 - n2))