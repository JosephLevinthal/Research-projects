x=int(input())
p=0
i=0
total= i+p
perp=0
perpi=0
while(x!=0):
	if(x%2==0):
		p=p+1
	else:
		i=i+1
	x=int(input())
	perp= (p/total)*100
	perpi=(i/total)*100
print(perp)
print(perpi)