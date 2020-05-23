x = int(input("Base: "))

for i in range(x):
	print((x - i) * "*" + 2 * i * "o" + (x - i) * "*")