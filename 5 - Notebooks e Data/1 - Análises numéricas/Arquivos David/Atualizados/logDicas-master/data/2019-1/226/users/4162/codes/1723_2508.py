n=int(input("insira o numero de series: "))
c=1
i=2
i1=3
i2=4
snl=+1
s=3
p=0
while c<n:
	p=snl*(4/(i*i1*i2))+p
	c=c+1
	i=i+2
	i1=i1+2
	i2=i2+2
	snl=snl*-1
f=s+p
print(round(f,8))








