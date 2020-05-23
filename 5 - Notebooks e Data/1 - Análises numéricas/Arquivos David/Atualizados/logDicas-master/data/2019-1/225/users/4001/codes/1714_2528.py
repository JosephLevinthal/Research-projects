n = int(input("N: "))
cont = 0
d = 0
n1 = 0
while (n > 0):
	n = n // 10
	cont = cont + 1
	n1 = n1 + (n % 10)
if (n < 10):
	n = n % 10
	cont = cont + 1
	n1 = n1 + (n % 10) ** cont
	
	