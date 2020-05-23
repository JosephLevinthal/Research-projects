from math import *
n = int(input('N: '))
e = 1
d = 3
c = 1
i = -1
pi = sqrt(12)
x = 1/(1*(3**0))

while (c<n):
	x = x+((i)*(1/(d*(3**e))))
	d = d+2
	e = e+1
	i *=-1
	c = c+1
y = pi*x
print(round(y, 8))