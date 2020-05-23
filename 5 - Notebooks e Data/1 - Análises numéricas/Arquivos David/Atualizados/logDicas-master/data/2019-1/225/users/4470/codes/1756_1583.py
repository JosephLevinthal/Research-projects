from numpy import*
a=str(input("numero:"))
i=1
x=0
s=""
while(x<len(a)):
	if(i==4):
		i=1
		s=s+"."
	s=s+a[x]
	i=i+1
	x=x+1
print(s)