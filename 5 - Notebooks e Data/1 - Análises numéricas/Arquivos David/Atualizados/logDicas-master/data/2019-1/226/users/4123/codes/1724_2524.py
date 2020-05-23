from math import*
x = int(input())
n = 4

while n<=x:
	if n%2 != 0:
		p = sin(pi/n)/sin((3*pi)/(2*n))
	else:
		p = sin(pi/n)/sin(2*pi/n)
	print(n,round(p,4))
	n += 1