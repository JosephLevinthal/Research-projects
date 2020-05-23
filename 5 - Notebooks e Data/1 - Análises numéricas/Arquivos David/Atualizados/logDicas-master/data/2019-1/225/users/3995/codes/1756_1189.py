v=input("qualquer:")
v=v.replace(' ','')
c=0
i=-1
j=1
n=""
while(i>=-len(v)):
	n=n+v[i]
	if(v[c]!=v[i]):
		j=0
	c=c+1
	i=i-1
print(v.upper())
print(j)