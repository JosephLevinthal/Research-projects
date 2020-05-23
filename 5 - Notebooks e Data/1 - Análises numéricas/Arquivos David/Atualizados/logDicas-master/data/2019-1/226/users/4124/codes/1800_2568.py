x = int(input("Nmr de asteriscos: "))
j = 0
for i in range(x):
	print((x*"*") + ("o" * j) + ("o" * j) + (x * "*"))
	x = x-1
	j = j + 1
	