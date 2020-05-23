n=float(input("digite um numero natural: "))
p=3
a=2
c=0
if(n==1):
	print(round(p, 8))
else:
	while(c<n-1):
		s=(-1)**c
		p=p+s*4/((a)*(a+1)*(a+2))
		c=c+1
		a=a+2
	print(round(p, 8))