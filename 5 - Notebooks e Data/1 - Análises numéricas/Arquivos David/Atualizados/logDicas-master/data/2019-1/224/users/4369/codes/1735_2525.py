n = int(input("Digite um numero: "))
c = 1
i = 0
if n == 1:
	print("1 divisor")
else:
	while c < n + 1:
		if n % c == 0:
			i = i +1
			print(c)
		c = c + 1
		
	print(i, "divisores")
		
	


	