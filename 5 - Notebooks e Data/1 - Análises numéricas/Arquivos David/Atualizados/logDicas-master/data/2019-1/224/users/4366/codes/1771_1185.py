from numpy import*
glicose=array(eval(input("digite os niveis de glicose:")))
i=0
cont=0
while(i<size(glicose)):
	if(glicose[i]>99):
		print(i)
		cont=cont+1
	i=i+1
print(cont)
	