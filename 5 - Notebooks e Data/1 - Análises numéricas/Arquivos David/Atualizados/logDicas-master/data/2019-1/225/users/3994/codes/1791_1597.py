from numpy import*
v=array(eval(input("Digite o custo: ")))
i=0
b=-5
c=0
while(i<size(v)):
	if(v[i]>=80):
		c=c+1
	else:
		c=c+0
	i=i+1
k = sum(v)+c*b
print(round(k,2))	
	
		
		
