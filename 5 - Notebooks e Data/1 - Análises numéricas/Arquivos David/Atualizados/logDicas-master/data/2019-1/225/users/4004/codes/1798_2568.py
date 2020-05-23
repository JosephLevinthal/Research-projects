x = int(input("valor: "))

y = 2

print(2 * x * "*")
for i in range((x - 1),0,-1):
	print(i * "*" + y * "o" + i * "*")
	y = y + 2