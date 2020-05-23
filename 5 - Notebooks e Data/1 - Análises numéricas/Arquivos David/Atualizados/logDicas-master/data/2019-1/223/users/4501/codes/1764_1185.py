from numpy import*
v=array(eval(input("vetor: ")))
i=0
cont=0
while(i<size(v)):
	if(v[i]>99):
		print(i)
		cont=cont+1
	i=i+1	
print(cont)	