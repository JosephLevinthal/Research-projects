n = int(input("metade do numero de asteriscos:"))
print(2 * n * "*")
j = 2
for i in range((n -1)  , 0 , -1):
	print(i * "*" + j * "o" + i * "*")
	j = j + 2