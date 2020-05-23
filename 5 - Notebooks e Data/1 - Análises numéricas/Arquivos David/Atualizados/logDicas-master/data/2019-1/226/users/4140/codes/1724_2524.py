n=int(input())
from math import *
i=4
while(i<=n):
	if(i%2!=0):
		p=(sin(pi/i))/(sin((3*pi)/(2*i)))
		print(i ,round(p,4))
	else:
		p=(sin(pi/i))/(sin((2*pi)/i))
		print(i ,round(p,4))
	i=i+1