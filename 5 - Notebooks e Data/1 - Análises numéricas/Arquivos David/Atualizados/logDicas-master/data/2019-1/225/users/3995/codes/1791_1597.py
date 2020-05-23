from numpy import*
v=array(eval(input("preco:")))

i=0
d=-5
m=0
while(i<size(v)):
	if(v[i]>=80):
		m=m+1
	else:
		m=m+0
	i=i+1
	
j=sum(v)+m*d
print(round(j,2))