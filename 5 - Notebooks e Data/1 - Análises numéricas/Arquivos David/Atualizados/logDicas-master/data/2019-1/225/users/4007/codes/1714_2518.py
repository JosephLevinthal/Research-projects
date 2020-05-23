n = int(input("pense em um numero: "))

while (n != 1):
	if (n > 0):
		if (n % 2 == 0):
			n = n // 2
			print(n)
			
		elif(n % 2 != 0):
			n = n * 3 + 1
			print(n)
			
			