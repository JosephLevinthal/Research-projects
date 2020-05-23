from numpy import*

vp=array(eval(input()))
vf=array(eval(input()))
			
i=0
while(i<11):
	if(vp[i]==max(vp)):
		print(i+1)
	i=i+1