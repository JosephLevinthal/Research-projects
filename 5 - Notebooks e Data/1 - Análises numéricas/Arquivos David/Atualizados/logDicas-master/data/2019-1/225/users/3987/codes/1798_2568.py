n = int(input("n:"))
j = 2
print((n*2) * "*")
for i in range((n-1),0,-1):
	print(i * "*" + j * "o" + i * "*")
	j = j + 2
	
	