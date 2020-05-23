from numpy import*
v=array(eval(input(" vetor de custos: ")))

i=0
s=0

while(i<size(v)):
	if(v[i]>80):
		s=s+(v[i]-5)
	else:
		s=s+v[i]
	
	i=i+1
print(round(s,2))
		