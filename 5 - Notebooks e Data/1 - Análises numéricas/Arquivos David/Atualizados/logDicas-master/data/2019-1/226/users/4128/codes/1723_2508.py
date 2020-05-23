h = int(input("insira um numero:"))

n = 0 
m = 0
x = 2
y = 3
z = 4
s = 2
while(n < h):
	f = 3 + m
	m = ((4)/(x * y * z)) *(-1)**s + m
	x = x + 2
	y = y + 2
	z = z + 2
	n = n + 1
	s = s + 1
print(round(f,8))	