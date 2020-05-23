from numpy import*
a = int(input())
f = "*"
d = "o"
g = 0
for i in range(a):
	b = f*(a-i) +d*g+ (f*(a-i))
	g += 2
	print(b)