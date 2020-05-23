from numpy import*
v=array(eval(input("presentes/mes:")))
j=array(eval(input("ausentes/mes:")))

i=0
c=1
while(v[i]!=max(v)):
	i=i+1
	c=c+1
print(c)
