from numpy import*
n = array(eval(input("turmas: ")))

i=0
c=0
for i in range(size(n)):
	if(n[i]%5==0):
		c=c+1
k=0
v = zeros(c, dtype=int)
for i in range(size(n)):
	if(n[i]%5==0):
		
		v[k]=i
		k = k+1
print(size(v))
print(v)
		
		
		
	

	
	
	
	
	
	
		
	
	