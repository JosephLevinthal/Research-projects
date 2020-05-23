n = int(input('Digite um numero: '))
pi = 3
t = 0
d1 = 2
d2 = 3
d3 = 4
i = 0
x = 0
while (t<n):
	pi = pi+x
	x = ((-1)**i)*(4/(d1*d2*d3))
	i = i+1
	d1 += 2
	d2 += 2
	d3 += 2
	t = t+1
	
print(round(pi, 8))