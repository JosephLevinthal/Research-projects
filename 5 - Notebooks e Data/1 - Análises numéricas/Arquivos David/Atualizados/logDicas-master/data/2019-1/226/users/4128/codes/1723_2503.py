h = int(input("insira um numero:"))
pi = 0
i = 0
x = 1
y = 2

while(i < h):
	pi = (4/x) *(-1)**y + pi
	i = i + 1
	x = x + 2 
	y = y + 1
print(round(pi, 8))