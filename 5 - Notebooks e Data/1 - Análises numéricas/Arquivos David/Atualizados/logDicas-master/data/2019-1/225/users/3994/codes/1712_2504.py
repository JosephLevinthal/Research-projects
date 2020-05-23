c=int(input("Quantidade inicial de copias de virus: "))
l=int(input("Quantidade inicial de leococitos: "))
v=int(input("Percentual de virus: "))
k=int(input("Percentual dos leucocitos: "))
d=0
while(l<2*c):
	j=(c*v)/100
	c=c+j
	a=(l*k)/100
	l=l+a
	d+=1
	if(l>=2*c):
		print(d)

	
	

