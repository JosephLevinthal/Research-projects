n=int(input("insira o numero de series: "))
c=0
i=1
snl=+1
p=0
while c<n:
	p=snl*(4/i)+p
	c=c+1
	i=i+2
	snl=snl*-1
print(round(p,8))

