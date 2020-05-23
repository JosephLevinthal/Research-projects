n =int(input("Numero: ")) 
for i in range(n):
	x = n * "*" + i * "o" + i * "o" + n * "*"
	print(x)
	n = n - 1