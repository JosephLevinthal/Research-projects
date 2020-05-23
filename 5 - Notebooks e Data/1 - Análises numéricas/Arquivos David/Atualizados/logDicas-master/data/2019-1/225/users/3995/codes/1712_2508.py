k=int(input("repeticao:"))
c=1
n=3.0
i=1
y=0
j=0
while(c<k):
	if(k>1):
		h=(((-1)**(i+1)))
		a=(4/((y+2)*(y+3)*(y+4)))
		w=(h*a)
	else:
		j=n
	c+=1
	i+=1
	y+=2
	j=j+w
print(round((j+n), 8))
