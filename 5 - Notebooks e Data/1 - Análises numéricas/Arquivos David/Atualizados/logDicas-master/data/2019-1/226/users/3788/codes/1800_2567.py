base = eval(input("Tamanho da base: "))

for j in range(0, base):
	for i in range(0, base - j):
		print("*", end="")
	print("\n", end="")
for j in range(0, base):
	for i in range(0, 1 + j):
		print("*", end="")
	print("\n", end="")

