n = int(input("base: "))
t = n
while t >= 1:
	print(t*"*")
	t = t - 1
t = 1
while t <= n:
	print(t*"*")
	t = t + 1
	