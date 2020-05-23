from math import*
n=int(input("insira o numero de series: "))
c=0
snl=+1
s=sqrt(12)
p=0
i=1
i1=0
while c<n:
	p=snl*(1/(i*(3**i1)))+p
	c=c+1
	i=i+2
	i1=i1+1
	snl=snl*-1
f=s*p
print(round(f,8))

