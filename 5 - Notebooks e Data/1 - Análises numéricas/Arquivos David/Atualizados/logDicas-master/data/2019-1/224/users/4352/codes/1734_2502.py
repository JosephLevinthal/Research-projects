from math import*
n=int(input("digite um numero: "))
x=1
c=0
s=0
i=0
if(n==1):
	print(round(sqrt(12), 8))
else:
	while(i<n):
		si=(-1)**i
		s=s+si*(1/(x*(3**c)))
		c=c+1
		x=x+2
		i=i+1
	print(round(sqrt(12)*s, 8))
	