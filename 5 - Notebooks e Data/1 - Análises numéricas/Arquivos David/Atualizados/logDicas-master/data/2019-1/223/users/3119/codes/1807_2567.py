a = int(input("Digite o numero: "))

for j in range(0, a):
	for i in range(0, a - j):
		print("*", end="")
	print("\n", end="")
	
for j in range(0, a):
	for i in range(0, j + 1):
		print("*", end="")
	print("\n", end="")	