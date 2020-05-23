from numpy import*
v = array(eval(input("vetor de media: ")))
i=0
k=1
m=0
while(i<size(v)):
	m= m + (v[i])**1/3 
	i=i+1
	
mc = (m/size(v))**3
print(round(mc,2))