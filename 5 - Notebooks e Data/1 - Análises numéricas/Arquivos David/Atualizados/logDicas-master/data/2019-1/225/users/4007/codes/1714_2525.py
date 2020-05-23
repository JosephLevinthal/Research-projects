n = int(input("digite um numero: "))
i = 1
a = 0
while (i <= n):
	if (n % i == 0):
		a = a + 1
		print(i)
		
	i = i + 1

if (a == 1):
	print(a, "divisor")

else:
	print(a, "divisores")

	