n = int(input())
s = 0
t = i = 1

while(i<=n):
	t = t*(i/(2*i+1))
	s += t
	i += 1
pi = 2*(s+1)
print(round(pi,10))