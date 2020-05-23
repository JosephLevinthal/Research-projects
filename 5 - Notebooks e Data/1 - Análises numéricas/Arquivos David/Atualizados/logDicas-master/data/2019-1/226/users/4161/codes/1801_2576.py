n = int(input("sequencia: "))
h = 0
for t in range(0,n):
	h = h + 1/(1+t)
print(round(h, 2))
	