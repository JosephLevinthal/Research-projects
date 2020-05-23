n=int(input("escreva um numero natural: "))
p=4
x=1
c=0
s=0
if(n==1):
	print(p)
else:
	while(c<n):
		si=(-1)**c
		s=s+si*(p/(x))
		x=x+2
		c=c+1
	print(round(s, 8))