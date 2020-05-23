n1 = int(input("Digite numero 1: "))
n2 = int(input("Digite numero 2: "))

if(((n1 * n2) % 2) == 0):
	s = n1 + n2
	print(s)
else:
	s = n2 - n1
	print(s)