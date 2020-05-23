n = int(input("Numero de Termos:"))
s = 2
c = 0
x = 2
y = 3
z = 4
m = 0
while(c < n):
	pi = 3 + m 
	m = ((4)/(x * y * z))*(-1)**s + m
	x = x + 2
	y = y + 2
	z = z + 2
	c = c + 1
	s = s + 1
print(round(pi, 8))
	