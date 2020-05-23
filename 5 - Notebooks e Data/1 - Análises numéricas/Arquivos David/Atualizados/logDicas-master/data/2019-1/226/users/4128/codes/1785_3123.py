from  numpy import*

v  = array(eval(input("numero;")))
z = 0
m = 0 
i = 0 
while(i != size(v)):
	m = ((v[i]**-1+ m)/size(v))**-1
	i = i + 1


	
print(round(m,2))