from numpy import*

glicose= array(eval(input()))

i=0
acima=0
while(i<size(glicose)):
	if(glicose[i]>99):
		print(i)
		acima=acima+1
	i=i+1
print(acima)