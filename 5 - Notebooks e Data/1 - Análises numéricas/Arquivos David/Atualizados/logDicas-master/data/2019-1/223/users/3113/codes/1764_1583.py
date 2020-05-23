from numpy import*
n=input("")

i=0
d=3
o="."
s=""
while(i<len(n)):
	if(i<(len(n)-4)):
		s=s+n[i:d]+o
	else:
		s=s+n[i:d]
	i=i+3
	d=d+3
		
print(s)