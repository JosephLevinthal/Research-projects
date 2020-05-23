n = int(input())

h = 0
for i in range(n):
	h += 1/(i+1)
print(round(h, 2))