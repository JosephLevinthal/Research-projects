from numpy import*
v= array(eval(input("Vetor:")))

i= 0
po= 0
a = 0
while(i < size(v)):
	if(v[i]>=0):
		po+=1
	i=i+1
v2= zeros(po,dtype=int)
i=0
while (i < size(v)):
	if(v[i]>=0):
		v2[a]=v[i]
		a+=1
	i+=1
print(v2)