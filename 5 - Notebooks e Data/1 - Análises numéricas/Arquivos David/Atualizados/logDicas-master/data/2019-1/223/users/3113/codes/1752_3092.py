q=input(" ")
V=3
E=2
D=1
g=q
k=0
s=0
while(g.upper!="X"):
	q=input("")
	if(q.upper()=="V"):
		s=s+3
	else:
		if(q.upper()=="E"):
			s=s+2
		else:
			if(q.upper()=="D"):
				s=s+1
	g=q
	k=s/100
print(k)