n = int(input())

s = 1.5
c1 = 1
m = 1
while(c1 < n):
	m = m + 2
	c1 = c1 + 1

while(n > 0):
	s = s * (n / m) + 1
	n = n - 1
	m = m - 2

print(round(s, 10))