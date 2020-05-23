from numpy import*
f=array(eval(input("vetor de frequencia: ")))
a=0
for v in f:
	if (v>=70):
		 a=a+1
va=zeros(a, dtype=int)
i=0
c=0
for v in f:
	if (v>=70):
		va[c]=i
		c=c+1
	i= i+1
print(a)
print(va)
	
	
	
	

