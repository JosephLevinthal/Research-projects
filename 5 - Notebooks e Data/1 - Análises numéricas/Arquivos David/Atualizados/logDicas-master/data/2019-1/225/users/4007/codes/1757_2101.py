n = int(input("digite o valor: "))
a, b = 0, 1
if(n > 2):
	while (b < n):
		print (b, end=" ")
		a, b = b, a + b