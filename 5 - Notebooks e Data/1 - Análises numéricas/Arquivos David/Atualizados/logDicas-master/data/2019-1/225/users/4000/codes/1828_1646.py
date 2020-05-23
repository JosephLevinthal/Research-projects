from numpy import*
x = array(eval(input("vetor: ")))
c=0
for i in range(size(x)):
	if (x[i]<=50):
		c = c+1
print(c)
v = zeros(c,dtype=int)
e=0
for i in range(size(x)):
	if(x[i]<=50):
		v[e]=i
		e = e+1
print(v)
	
		
		
	
		
	

		

		
	

	

	
	
	

	
	
	
	
	
		
		
	