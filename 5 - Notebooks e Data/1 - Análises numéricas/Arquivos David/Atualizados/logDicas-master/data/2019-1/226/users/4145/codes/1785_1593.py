from numpy import*
v = array(eval(input("vetor de notas: ")))
#v=input("vetor de notas: ")
#vv=arange(v,dtype ==float)
i=1
n=0
c=0
d=0

while(i<size(v)):
	v[c]=   v[c]*i 
	c=c+1
	d=d+i
	i=i+1
m =sum(v)/d	
#print(round(n/d,2))	
print(round(m,2))