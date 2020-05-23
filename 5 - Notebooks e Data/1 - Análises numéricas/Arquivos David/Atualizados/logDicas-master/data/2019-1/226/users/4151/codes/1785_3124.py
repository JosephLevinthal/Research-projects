from numpy import*
v=array(eval(input("digite um vetor: ")))
i=0
m=0
	

while(i<size(v)):
	m=m+v[i]
	i=i+1
x=m**(1/size(v))
print(round(x,2))

	