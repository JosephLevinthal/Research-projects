from numpy import*
s=array(eval(input("")))
i=0
i1=0
while(i<size(s)):
	if(s[i]==max(s)):
		e=i1
	i=i+1
	i1=i1+1
print(e)