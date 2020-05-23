v=int(input("virus:"))
l=int(input("leucocitos:"))
v1=float(input("percentual de v:"))
l1=float(input("percentual de l:"))
t=0
while(l<2*v):
	h=(v*v1)/100
	v=v+h
	w=(l*l1)/100
	l=l+w
	t=t+1
	if(l>=2*v):
		print(t)
	