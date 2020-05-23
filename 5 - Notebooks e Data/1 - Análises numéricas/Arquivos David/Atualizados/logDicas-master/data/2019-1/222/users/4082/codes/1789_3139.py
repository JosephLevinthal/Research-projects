from numpy import*
v= array(eval(input("n numeros positivos")))
i=0
a=size(v)
c=0
while(i < a):
	c=c+v[1]**3
	i=i+1
g= (c/a)**2	 
print(round,(g,2))
	