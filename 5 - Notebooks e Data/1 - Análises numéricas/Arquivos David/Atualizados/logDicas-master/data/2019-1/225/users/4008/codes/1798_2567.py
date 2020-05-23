n = int(input("n: "))
c = n
while(c>0):
	t = ""
	for i in range(c):
		t = t + '*'
	c = c - 1
	print(t)
c=1
while(c<=n):
	g = ""
	for i in range(c):
		g = g + '*'
	c = c + 1
	print(g)