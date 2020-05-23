n = int(input("Numero de termos:"))

h = 0
x = 3
y = 0
f = 1

while(h < n):
	pi = 4/1 + y
	y = y + (4/x)*((-1)**f)
	x = x + 2
	h = h + 1
	f = f + 1
print(round(pi, 8))
	