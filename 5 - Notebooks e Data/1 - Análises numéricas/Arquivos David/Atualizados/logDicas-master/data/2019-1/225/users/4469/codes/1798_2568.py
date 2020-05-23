m = int(input())

n = m * 2
no = 2

print(n * "*")
for i in range(m - 1, 0, -1):
	print(i * "*" + no * "o" + i * "*")
	no = no + 2