n = int(input())
a = [1,0]
b = [1/2**0.5,0]
t = [0.25,0]
p = [1,0]
pi = [0,0]
nn = 1
nv = 0
i = 1
while i<=n:
	a[nn] = (a[nv] + b[nv])/2
	b[nn] = (a[nv]*b[nv])**0.5
	t[nn] = t[nv] - p[nv]*((a[nv]-a[nn])**2)
	p[nn] = 2*p[nv]
	pi[nn] = ((a[nv]+b[nv])**2)/(4*t[nv])
	a[nv] = a[nn]
	b[nv] = b[nn]
	t[nv] = t[nn]
	p[nv] = p[nn]
	pi[nv] = pi[nn]
	print(round(pi[nn],14))
	i+=1
