x=int(input("numero:"))
c=0 #total de numeros
p=0
i=0
while(x!=0):
	if(x%2==0):
		p=p+1
	else:
		i=i+1
	c=c+1
	x=int(input("numero:"))
if(p>=0 and i>=0):
	d=(p/c)*100
	print(round(d,2))
	e=(i/c)*100
	print(round(e, 2))