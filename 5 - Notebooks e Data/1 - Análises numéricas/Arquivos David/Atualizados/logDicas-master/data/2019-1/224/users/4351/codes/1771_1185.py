from numpy import*
glicose=array(eval(input("digite os niveis de glicose: ")))
c=0
i=0
while(i<size(glicose)):
	if(glicose[i]>99):
		print(i)
		c=c+1
	i=i+1
print(c)