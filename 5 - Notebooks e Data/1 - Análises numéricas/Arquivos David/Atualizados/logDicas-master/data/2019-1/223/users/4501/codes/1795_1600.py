from numpy import*
v=array(eval(input("custo: ")))
i=0
a=0
b=0
while(i<size(v)):
	if(v[i]>80):
		v=v+(a[i])*(15/100)
	else:
		b=b+(a[i])
	i=i+1	
p=v+b
print(round(p, 2))	
		
		